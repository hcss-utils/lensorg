# -*- coding: utf-8 -*-
import os
import requests
from ratelimit import limits, sleep_and_retry
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
token = os.environ.get("LENSAPI")


def chunks(lst, n=999):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


@sleep_and_retry
@limits(calls=9, period=60)
def remote_call(dois, token):
    """Get fields of study using a list of dois.
    
    Parameters
    ----------
    dois: list[str]
        list of valid DOIs
    token: LENS' API private token


    Notes
    -----
    API has a limit of 1000 records per call, 10 calls per minute, 
    5000 calls per month. 
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = """{
        "query": {
            "terms": {
                "doi": REPLACE
            }
        },
        "size": 1000,
        "include": ["fields_of_study", "external_ids"]
    }""".replace("REPLACE", str(dois).replace("'", '"'))
    response = requests.post(
        "https://api.lens.org/scholarly/search", 
        data=data, 
        headers=headers
    )
    return response.json()


def process(response):
    """Yield processed article items"""
    data = response["data"]
    for item in data:
        yield {
            "doi": "".join(
                doi["value"] 
                for doi in item["external_ids"] 
                if doi["type"]=="doi"
            ),
            "fields": "_".join(item.get("fields_of_study", "")) or "No data."
        }
