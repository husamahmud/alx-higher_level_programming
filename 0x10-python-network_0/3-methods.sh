#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS google.com | grep "Allow:" | cut -c 8-
