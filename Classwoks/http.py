import json
from dataclasses import dataclass

import requests

APP_ID = "63e6c6d407cd3a188b97d259"
base_url = "https://dummyapi.io/data/v1/"
HEADER = {"app-id": APP_ID}


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    gender: str
    id: str| None = None


def get_user_data(user_id: str):
    print("call external api")
    r = requests.get(base_url + "user/" + user_id, headers=HEADER)
    return r.json()


def get_user_basic_details(user_id: str) -> User:
    data = get_user_data(user_id)
    user = User(
        id=data["id"],
        first_name=data["firstName"],
        last_name=data["lastName"],
        email=data["email"],
        phone=data["phone"],
        gender=data["gender"],
    )

    return user

def create_user(user: User) -> User:
    usr_data = {
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email,
        "phone": user.phone,
        "gender": user.gender
    }

    c = requests.post(base_url + "user/create", headers=HEADER, data=usr_data)

    usr_json = c.json()

    return User(
        id=usr_json["id"],
        first_name=usr_json["firstName"],
        last_name=usr_json["lastName"],
        email=usr_json["email"],
        phone=usr_json["phone"],
        gender=usr_json["gender"]
    )




def update_user_first_name(user_id: str, name: str) -> User:
    pass


def search_users_by_name(name: str) -> User | None:
    pass


if __name__ == "__main__":

    # user = get_user_basic_details("64120e130a36315418733acb")
    # print(user)

    print(create_user(User(
        first_name="Johnsd",
        last_name="Johnssdon",
        email="johnsdson@mail.com",
        phone="12342567",
        gender="male"
    )))