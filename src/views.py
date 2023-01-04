"""Views module"""

import json
from src.services import CreateCardService
from flask_restful import Resource, reqparse

from src.trello.interface import CategoryInterface, ListInterface


parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True, help='Type must be included')
parser.add_argument('title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('category', type=str)


class Card(Resource):
    def get(self):
        return { 'success': True }

    def post(self):
        args = parser.parse_args()
        return CreateCardService(
            type=args['type'],
            title=args['title'],
            desc=args['description'],
            category=args['category']).call()


class SetCategories(Resource):
    def post(self):
        result = CategoryInterface.create_missing_categories()
        return { 'categories': json.loads(result)}


class SetList(Resource):
    def post(self):
        result = ListInterface.create_todo_if_missing()
        return { 'lists': json.loads(result)}
