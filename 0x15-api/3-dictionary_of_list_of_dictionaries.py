#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    employees = requests.get(base_url + "users").json()

    # Create a dictionary with user ID as keys and todo lists as values
    all_todos = {
            employee.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee.get("username")
                } for todo in requests.get(base_url + "todos", params={
                    "userId": employee.get("id")}).json()]
            for employee in employees
            }

    # Write the dictionary to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_todos, jsonfile)
