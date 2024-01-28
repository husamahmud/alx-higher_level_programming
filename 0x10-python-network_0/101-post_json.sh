#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -sI -H "Content-Type: application/json" -d @"$2" -X POST "$1"
