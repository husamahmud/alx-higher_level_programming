#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -d "$2" -X POST "$1"
