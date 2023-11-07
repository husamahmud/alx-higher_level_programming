#!/usr/bin/python3
"""A script to add all arguments to a list, and then save them to a file"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    json_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, 'add_item.json')
