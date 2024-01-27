#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$status_code" == 200 ]; then
	echo $(curl -s "$1")
fi
