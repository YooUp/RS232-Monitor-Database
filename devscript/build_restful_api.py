#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os

INPUT_FILE = 'database/monitors.json'
INPUT_FOLDER = 'database/monitors/'
RESTFULL_FOLDER = 'restful/'
OUTPUT_FILE = 'restful/monitors.json'
OUTPUT_FOLDER = 'restful/monitors/'

def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')

    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data

def save_json(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data, separators=(',', ':')))

def main():
    os.mkdir(RESTFULL_FOLDER)
    os.mkdir(OUTPUT_FOLDER)
    
    save_json(OUTPUT_FILE, read_json(INPUT_FILE))
    
    database_files = [INPUT_FOLDER + f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    for database_file in database_files:
        save_json(OUTPUT_FOLDER + os.path.basename(database_file), read_json(database_file))

if __name__ == "__main__":
    main()