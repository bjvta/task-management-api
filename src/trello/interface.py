"""Trello Endpoints module"""

from src.helpers import EnhancedJSONEncoder
import random
import json

from .endpoints import create_card, create_category, create_list, get_categories, get_lists, get_members


class CategoryInterface:
    @staticmethod
    def all():
        return json.dumps(get_categories(), cls=EnhancedJSONEncoder)

    @staticmethod
    def create(name, color):
        return create_category(name, color)

    @staticmethod
    def create_missing_categories():
        categories = get_categories()
        missing_categories = [{'name': 'issue', 'color': 'purple' },
                              {'name': 'bug', 'color': 'red'},
                              {'name': 'task', 'color': 'blue'}]

        for missing_category in missing_categories:
            for category in categories:
                if category.name == missing_category['name']:
                    missing_categories.remove(missing_category)

        for category in missing_categories:
            create_category(category['name'], category['color'])
        return json.dumps(get_categories(), cls=EnhancedJSONEncoder)

    @staticmethod
    def get_or_create(name):
        categories = get_categories()
        for category in categories:
            if category.name == name:
                return category.id
        category = create_category(name, 'blue')
        return category['id']




class ListInterface:
    @staticmethod
    def all():
        return get_lists()

    @staticmethod
    def get_id_by_name(name):
        lists = json.loads(get_lists())
        for list_obj in lists:
            if list_obj['name'] == name:
                return list_obj['id']
        return 'unknown'

    @staticmethod
    def create_todo_if_missing():
        lists_with_conversion = get_lists()
        lists = json.loads(lists_with_conversion)
        for list_obj in lists:
            if list_obj['name'] == 'TODO':
                return lists_with_conversion
        create_list('TODO')
        return get_lists()


class MemberInteface:
    @staticmethod
    def all():
        return get_members()

    @staticmethod
    def get_random():
        return random.choice(get_members())


class CardInterface:
    @staticmethod
    def create(query):
        return create_card(query)
