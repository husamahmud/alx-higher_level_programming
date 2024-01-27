#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -sI -X "${1}" | grep "Allow:" | cut -c 8-
