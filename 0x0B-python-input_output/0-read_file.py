#!/usr/bin/python3

def read_file(filename=""):
    with open('my_file_0.txt', mode='r', encoding='utf-8') as myfile:
        print(myfile.read())
