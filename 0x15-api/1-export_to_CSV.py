#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
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
    todos = requests.get(
            base_url + "todos", params={"userId": employee_id}).json()

    # Write todos to CSV file
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
            [employee_id, username, task.get("completed"), task.get("title")]
            ) for task in todos]
