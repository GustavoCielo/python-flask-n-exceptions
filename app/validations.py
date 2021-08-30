import os
from json import dump


def path_exists():
    if not os.path.exists("./app/database/database.json"):
        os.makedirs("./app/database/")
        with open("./app/database/database.json", "w") as f:
            dump({"data": []}, f, indent=4)
            return {"data": []}, 200


def database_empty():
    if os.path.exists("./app/database/database.json"):
        if not os.stat("./app/database/database.json").st_size:
            with open("./app/database/database.json", "w") as f:
                dump({"data": []}, f, indent=4)
                return {"data": []}, 200


def path_exists_request(user):
    if not os.path.exists("./app/database/database.json"):
        os.makedirs("./app/database/")
        with open("./app/database/database.json", "w") as f:
            dump({"data": [user.__dict__]}, f, indent=4)
            return {"data": [user.__dict__]}, 200
