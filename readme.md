### Coding Assigment

### Database

Array is used instead of real database for operation.

### Gets started

#### Running without docker

```
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requirements.txt
flask run
```

#### Running with docker

```
docker build -t api-todo .
docker run -p 5000:5000 -d api-todo
```

#### Run unit test

```
pytest
```

### Todo Data Structure

```
id: unique id (using increment)
title: string
description: string
finished_at: dateTime (format d-m-Y H:i:s)
created_at: dateTime (format d-m-Y H:i:s)
updated_at: dateTime (format d-m-Y H:i:s)
deleted_at: dateTime (format d-m-Y H:i:s)
```

### API Schema

* /todo (POST) create todo
  ```
  Sample Request : 
  {
    "title": "Task Title",
    "description": "Description of task"
  }
  ```
* /todo (GET) get all todo
* /todo/<id> (GET) get todo by id
* /todo/<id> (PUT/PATCH) update Todo
  ```
  Sample Request : 
  {
    "title": "Task Title update",
    "description": "Description of task update"
  }
  ```
* /todo/<id>/finish (any method except delete) finish todo
* /todo/<id> (DELETE) soft delete todo

### Folder Structure

```
.
├── app.py
├── requirements.txt
├── public
├── test
    └── models.py       //data models define
└── todo
    ├── models.py       //data models define
    ├── mapping.go      //response computing & format
    ├── routers.go      //router binding
    └── repository.go   //DB Operation
```