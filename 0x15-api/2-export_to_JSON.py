#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    # Get user ID from command line argument
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    username = user.get("username")

    # Fetch todos for the user
    todo_list = requests.get(
            base_url + "todos", params={"userId": employee_id}).json()

    # Write todos to JSON file
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
            } for task in todo_list]}, jsonfile)
