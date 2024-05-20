#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f"Employee {user_data['name']} is done with tasks"
            f" ({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")
