#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os

OUTPUT_FOLDER = 'build/'
MONITORS_FOLDER = 'monitors/'


def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')

    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))


def main(file_name):
    os.makedirs(OUTPUT_FOLDER)
    os.makedirs(OUTPUT_FOLDER + MONITORS_FOLDER)

    data = read_json(file_name)
    save_json(OUTPUT_FOLDER + file_name, data)
    
    for monitor in data['monitors']:
        save_json(OUTPUT_FOLDER + MONITORS_FOLDER + monitor['name'].lower().replace(' ','_') + ".json", monitor)
     

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise Exception("This program needs the database to check in parameter")
    main(sys.argv[1])