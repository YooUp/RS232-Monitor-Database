#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os


def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')

    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))


def main(database_file):
    data = read_json(database_file)
    missing_fields = []
    
    if not "version" in data:
        missing_fields.append(" - Mandatory field 'version' is missing in the database\n")
        
    if not "monitors" in data:
        missing_fields.append(" - Mandatory field 'monitors' is missing in the database\n")
    else:
        for monitor in data['monitors']:
            if not "name" in monitor:
                missing_fields.append(" - Mandatory field 'name' is missing for the monitor at rank %d\n" % data['monitors'].index(monitor))
            if not "baudrate" in monitor:
                missing_fields.append(" - Mandatory field 'baudrate' is missing for the monitor %s\n" % monitor['name'])
            if not "doc" in monitor:
                missing_fields.append(" - Mandatory field 'doc' is missing for the monitor %s\n" % monitor['name'])
            if not "commands" in monitor:
                missing_fields.append(" - Mandatory field 'commands' is missing for the monitor %s\n" % monitor['name'])

    if len(missing_fields) > 0:
        message = "Some mandatory fields are missing:\n"
        for missing_field in missing_fields:
            message = message + missing_field
        raise Exception(message)
    
    print("No mandatory field is missing")

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise Exception("This program needs the database to check in parameter")
    main(sys.argv[1])