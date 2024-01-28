#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
