#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os

MONITORS_FILE = 'MONITORS.md'


def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')

    with open(file_name, 'r') as file:
        data = json.loads(file.read())
    return data


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))
        
        
def save_txt(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)


def main(file_name):
    if(os.path.isfile(MONITORS_FILE)):
        os.remove(MONITORS_FILE)
    
    data = read_json(file_name)
    content = "# Supported Monitors\n\n"
    
    for monitor_name in sorted([monitor['name'] for monitor in data['monitors']]):
        content = content + ("- %s\n" % monitor_name)
    
    save_txt(MONITORS_FILE, content)
     

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise Exception("This program needs the database to check in parameter")
    main(sys.argv[1])