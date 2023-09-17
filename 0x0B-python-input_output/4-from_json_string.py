#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a From JSON string to Object"""
import json

def from_json_string(my_str):
    """Return an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)