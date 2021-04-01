#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os

INPUT_FOLDER = 'database/monitors/'

def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')

    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))


def main():
    missing_fields = []
    
    database_files = [INPUT_FOLDER + f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    for database_file in database_files:
        data = read_json(database_file)

        if not "name" in data:
            missing_fields.append(" - Mandatory field 'name' is missing in file %s\n" % database_file)
        if not "doc" in data:
            missing_fields.append(" - Mandatory field 'doc' is missing in file %s\n" % database_file)
        if not "baudrate" in data:
            missing_fields.append(" - Mandatory field 'baudrate' is missing in file %s\n" % database_file)
        if not "stopbit" in data:
            missing_fields.append(" - Mandatory field 'stopbit' is missing in file %s\n" % database_file)
        if not "parity" in data:
            missing_fields.append(" - Mandatory field 'parity' is missing in file %s\n" % database_file)
        if not "commands" in data:
            missing_fields.append(" - Mandatory field 'commands' is missing in file %s\n" % database_file)

    if len(missing_fields) > 0:
        message = "Some mandatory fields are missing:\n"
        for missing_field in missing_fields:
            message = message + missing_field
        raise Exception(message)
    
    print("No mandatory field is missing")

if __name__ == "__main__":
    main()