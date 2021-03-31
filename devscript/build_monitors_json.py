#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os

INPUT_FOLDER = 'database/monitors/'
OUTPUT_FILE = 'database/monitors.json'
DEFAULT_DATA =  {
                    'version':1,
                    'monitors':[]
                }

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

    try:
        data = read_json(OUTPUT_FILE)
        data['monitors'] = []
        data['version'] = data['version'] + 1
    except:
        data = DEFAULT_DATA
    
    database_files = [INPUT_FOLDER + f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    for database_file in database_files:
        monitor = read_json(database_file)
        data['monitors'].append(monitor)
    
    save_json(OUTPUT_FILE, data)
    print(data['version'])

if __name__ == "__main__":
    main()
    