"""Trello Endpoints module"""

import requests
import json
from dotenv import dotenv_values
from .models import Category

config = dotenv_values(".env")

TRELLO_API_KEY = config['TRELLO_API_KEY']
TRELLO_TOKEN = config['TRELLO_TOKEN']
TRELLO_BOARD_ID = config['TRELLO_BOARD_ID']

query = {
      'key': TRELLO_API_KEY,
      'token': TRELLO_TOKEN
    }

BASE_URL = f"https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/"

"""
Categories / Labels
"""

def get_categories():
    url = f"{BASE_URL}/labels"
    response = requests.request("GET", url, params=query)
    categories = []
    for data in json.loads(response.text):
        category = Category(data['id'], data['name'], data['color'])
        categories.append(category)
    return categories


def create_category(name, color):
    url = "https://api.trello.com/1/labels"
    iquery = {
      'name': f"{name}",
      'color': f"{color}",
      'idBoard': f"{TRELLO_BOARD_ID}",
    }

    query.update(iquery)
    response = requests.request(
       "POST",
       url,
       params=query
    )
    return json.loads(response.text)

"""
Lists
"""

def get_lists():
    url = f"{BASE_URL}/lists"
    headers = {"Accept": "application/json" }
    response = requests.request("GET", url, headers=headers, params=query)
    return response.text


def create_list(name):
    url = "https://api.trello.com/1/lists"
    iquery = {
      'name': f"{name}",
      'idBoard': TRELLO_BOARD_ID,
    }
    query.update(iquery)
    response = requests.request("POST", url, params=query)
    return response.text

"""
Members
"""

def get_members():
    url = f"{BASE_URL}/members"
    response = requests.request("GET", url, params=query)
    return json.loads(response.text)


"""
Cards
"""

def create_card(iquery):
    url = "https://api.trello.com/1/cards"

    headers = {"Accept": "application/json"}
    query.update(iquery)

    response = requests.request(
       "POST",
       url,
       headers=headers,
       params=query
    )
    return json.loads(response.text)


