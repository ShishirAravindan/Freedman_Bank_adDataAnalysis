"""
Script that extracts relevant data from the comprehensive advertisement data .CSV file.
"""

import json
import os


def getAllAdTexts(fileName: str):
    """
    Returns dictionary with key as identifier and value as text of all ad data
    all the ad texts will be converted into lowercase for processing
    """
    parentDir = os.path.dirname(os.getcwd())
    path_to_JSON = os.path.join(parentDir, f"data_src/{fileName}.json")
    with open(path_to_JSON, 'r') as f:
        data = json.load(f)
    result = {}
    for ad in data:
        identifier = ad['identifier']
        text = ad['Text']
        if identifier not in result:
            result[identifier] = text.lower()
    return result