#!/bin/bash
# This script will send a POST request to a URL passed as an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
