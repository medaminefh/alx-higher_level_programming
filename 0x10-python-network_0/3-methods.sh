#!/bin/bash
# This script will send a request to a URL passed as an argument, and displays the body of the response
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
