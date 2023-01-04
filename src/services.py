"""SErvices moduel"""

from src.helpers import CreateBugNameHelper
from src.trello.interface import CardInterface, CategoryInterface, ListInterface, MemberInteface


class CreateCardService:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.title = kwargs['title']
        self.desc = kwargs['desc']
        self.category = kwargs['category']
        self.member_id = MemberInteface.get_random()['id']
        self.list_id = ListInterface.get_id_by_name('TODO')

    def call(self):
        query = self.prepare_query()
        new_card = CardInterface.create(query)
        return new_card

    def prepare_query(self):
        return {
            'idList': self.list_id,
            'idMembers': self.set_members(),
            'name': self.set_name(),
            'desc': self.desc,
            'idLabels': self.set_labels()
        }

    def set_name(self):
        if self.type == 'bug':
            return CreateBugNameHelper(self.desc).call()
        else:
            return self.title


    def set_labels(self):
        if self.type == 'task':
            return [CategoryInterface.get_or_create(self.category)]
        elif self.type == 'bug':
            return [CategoryInterface.get_or_create('bug')]
        return []

    def set_members(self):
        if self.type == 'issue':
            return []
        else:
            return [self.member_id]
