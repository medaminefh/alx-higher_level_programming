#!/usr/bin/python3
"""lockedclass module"""
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

try:
    args = load_from_json("add_item.json")
except Exception:
    args = []
args.extend(sys.argv[1:])
save_to_json(args, "add_item.json")
