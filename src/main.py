
from flask import Flask
from flask_restful import Resource, Api
from .views import *

app = Flask(__name__)
api = Api(app)


api.add_resource(Card, '/')
api.add_resource(SetCategories, '/load_categories')
api.add_resource(SetList, '/load_lists')

if __name__ == '__main__':
    app.run(debug=True)

