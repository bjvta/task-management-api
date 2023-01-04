# Task Management Trello Integration

This project allows to create three types of cards on a Trello Board, and for that you will need:

- TRELLO API KEY
- TRELLO TOKEN
- TRELLO BOARD ID

If you do not know how to get it, please go to this [link](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#cards)



## Setup and Installation

### Clone Repository
```
git clone git@github.com:bjvta/task-management-api.git && cd task-management-api
```
### Add the virtualenv 

```
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

### Install dependencies

```
pip3 install -r requirements.txt
```

### Create .env file from .env.example and set your Trello keys

```
cp .env.example .env
```

### Run the server
```
make runserver
# You should get this

    flask --app src.main --debug run
    * Serving Flask app 'src.main'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 102-600-632

```


## Endpoints:

- API status
```
GET: /
This endpoint return a { 'success' : true }
```


- Load Categories
```
POST: /load_categorires
This endpoint will load missing labels in trello, like: issue, bug and task
```

- Load List
```
POST: /load_lists
This endpoint will load missing list like `TODO`
```


- Create Card
```
POST: /
This endpoint will create a card and the body should be

For an issue:
- type : string : required
- title : string
- description : string

For a bug:
- type : string : required
- description : string

For a task:
- type : string : required
- title : string
- category: string

```

### Load Postman Collection

You can load the postman collection from the file `postman_collection.json`


## Happy Coding!!!