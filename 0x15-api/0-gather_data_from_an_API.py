#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_id = sys.argv[1]
    user = requests.get(base_url + "users/{}".format(user_id)).json()

    # Get todos for the user
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    # Get list of completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print summary of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
