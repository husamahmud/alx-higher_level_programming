#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -si -X OPTIONS google.com | grep "Allow:" | cut -c 8-
