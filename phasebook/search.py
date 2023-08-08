from flask import Blueprint, request

from .data.search_data import USERS

import sys



bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    filtered_users = USERS

    if args:

        filtered_users = []

        for key, value in args.items():
            for user in USERS:
                if check_value(key, value, user):
                    if (check_unique(filtered_users, user)):
                        filtered_users.append(user)

    return filtered_users

# Checks if user matches the search preferences

def check_value(key, value, user):

    match key:
        case "id":
            if value == user[key]:
                return True
        case "name":
            if value.lower() in user[key].lower():
                return True
        case "age":
            if int(value) >= user[key] - 1 and int(value) <= user[key] + 1:
                return True
        case "occupation":
            temp = user[key] + "er"
            if value.lower() in temp.lower():
                return True

    return False

# Checks if user that is being appended is unique or not

def check_unique(filtered_users, user):
    for filtered_user in filtered_users:
        if filtered_user["id"] == user["id"]:
            return False
    return True