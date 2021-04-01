#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os

INPUT_FOLDER = 'database/monitors/'
OUTPUT_FILE = 'database/monitors.json'

def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')

    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data


def main():

    try:
        data = read_json(OUTPUT_FILE)
        version = data['version'] + 1
        os.remove(OUTPUT_FILE)
    except:
        version = 1
    
    with open(OUTPUT_FILE, 'w') as output_file:
    
        output_file.write('{\n\t"version":%d,\n\t"monitors":[\n' % version)
    
        database_files = [INPUT_FOLDER + f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
        last = len(database_files)-1
        for index, database_file in enumerate(database_files):

            with open(database_file, 'r') as input_file:
                for line in input_file.readlines():
                    output_file.write("\t\t%s" % line)
            
            if not last is index:
                output_file.write(',')
            output_file.write('\n')
            
        output_file.write('\t]\n}')
    
    print(version)

if __name__ == "__main__":
    main()
    