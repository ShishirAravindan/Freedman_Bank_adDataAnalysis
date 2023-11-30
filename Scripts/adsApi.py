"""
Script that extracts relevant data from the comprehensive advertisement data .CSV file.
"""

import pandas as pd
import json
import os

def _convertExcelToJSON(source, target):
    df = pd.read_excel(source)
    df['identifier'] = df['identifier'].astype(int)
    JSONData = df.to_json(orient='records')

    with open(target, 'w') as JSONFile:
        JSONFile.write(JSONData)


def getAllAdTexts(fileName: str):
    """
    Returns dictionary with key as identifier and value as text of all ad data
    all the ad texts will be converted into lowercase for processing
    """
    parentDir = os.path.dirname(os.getcwd())
    path_to_JSON = os.path.join(parentDir, f"data_src/{fileName}.json")

    if not os.path.exists(path_to_JSON):
        excelFilePath = os.path.join(parentDir, "data_src", f"{fileName}.xlsx")
        _convertExcelToJSON(excelFilePath, path_to_JSON)

    with open(path_to_JSON, 'r') as f:
        data = json.load(f)
    result = {}
    for ad in data:
        identifier = ad['identifier']
        text = ad['Text']
        if identifier not in result:
            result[identifier] = text.lower()
    return result