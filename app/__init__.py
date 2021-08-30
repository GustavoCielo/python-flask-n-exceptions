import os
from json import load, dump
from flask import Flask, request
from app.classes import User
from app.validations import database_empty, path_exists, path_exists_request

app = Flask(__name__)


@app.get("/")
def home():
    return "<h1>Hello flask</h1>"


@app.get("/user")
def user_get():
    database_empty()
    path_exists()

    if os.path.exists("./app/database/database.json"):
        with open("./app/database/database.json", "r") as f:
            return load(f), 200


@app.post("/user")
def create_user():
    data = request.get_json()

    user = User(**data)

    if type(user.email) != str or type(user.nome) != str:
        return {
            "wrong fields": [
                {
                    "nome": str(type(user.nome)).split("'")[1]
                },
                {
                    "email": str(type(user.email)).split("'")[1]
                }
            ]
        }, 400

    user.nome = user.nome.title()
    user.email = user.email.lower()

    path_exists_request(user)

    with open("./app/database/database.json", "r") as f:
        opened_file = load(f)

    json_file = opened_file["data"]
    for item in json_file:
        if item["email"] == user.email:
            return {"error": "User already exists."}, 409

    with open("./app/database/database.json", "w") as f:
        json_file.append(user.__dict__)
        dump(opened_file, f, indent=4)
        return {"data": user.__dict__}, 201
