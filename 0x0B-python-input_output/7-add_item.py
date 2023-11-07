#!/usr/bin/python3
"""A script to add all arguments to a list, and then save them to a file"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
json_f = 'add_item.json'
save_to_json_file(args, json_f)
loaded_data = load_from_json_file(json_f)
