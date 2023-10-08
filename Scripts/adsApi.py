"""
Created a script containing a bunch of functions useful for extracting relevant data from the csv file.
"""
import pandas as pd
import json
import csv


def getAllAdTexts():
    """
    Returns dictionary with key as identifier and value as text of all ad data
    all the ad texts will be converted into lowercase for processing
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
    result = {}
    for ad in data:
        identifier = ad['identifier']
        text = ad['Text']
        if identifier not in result:
            result[identifier] = text.lower()
    return result


def getAdByID(id: int):
    """
    Returns the ad dictionary given an unique identifier,
    if identifier does not exist, returns None
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
    for ad in data:
        if ad['identifier'] == str(id):
            return ad
    return None


def getFSBAds():
    """
    Returns list[int] of ad identifiers where the bank is Freedman's Savings bank.
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
    result = []
    for ad in data:
        title = ad['Title'].lower()
        text = ad['Text'].lower()
        if 'freedman' in title or 'freedmen' in title:
            result.append(int(ad['identifier']))
        if 'fsb' in text:
            result.append(int(ad['identifier']))
    return result


def getOtherAds():
    """Returns list[int] of ad identifiers where the bank is not Freedman's Savings bank."""
    with open('db.json', 'r') as f:
        data = json.load(f)
    result = []
    fsb_adds = getFSBAds()
    for ad in data:
        if int(ad['identifier']) not in fsb_adds:
            result.append(int(ad['identifier']))
    return result


