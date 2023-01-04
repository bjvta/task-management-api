"""Helpers module"""


import dataclasses, json
from datetime import datetime

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


class CreateBugNameHelper:
    def __init__(self, name):
        self.name = name

    def call(self):
        first_word = self.name.split(' ')[0]
        day = datetime.now().day
        month = datetime.now().month
        return f"bug-{first_word}-{day}{month}"

