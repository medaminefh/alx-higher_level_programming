#!/bin/bash
# This script will send a POST request to a URL passed as an argument
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
