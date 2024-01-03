#!/usr/bin/python3
"""
Script to fetch employee TODO list progress from
the JSONPlaceholder API and export it to a CSV file.

Usage: python3 script.py <employee_id>

This script fetches user information and their
TODO list from the JSONPlaceholder API,
calculates the progress, and exports the data to a CSV file.

Author: Your Name
"""

import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from
    the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of dictionaries containing task details.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Fetch user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Collect TODO progress data
    todo_progress_data = []
    for task in todo_data:
        task_data = {
            "USER_ID": employee_id,
            "USERNAME": user_data.get('username', 'Unknown'),
            "TASK_COMPLETED_STATUS": str(task.get('completed', False)),
            "TASK_TITLE": task.get('title', 'Untitled')
        }
        todo_progress_data.append(task_data)

    return todo_progress_data


def export_to_csv(employee_id, todo_progress_data):
    """
    Exports employee TODO progress data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        todo_progress_data (list): List of
        dictionaries containing task details.

    Returns:
        None
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = [
                "USER_ID", "brucetravis",
                "TASK_COMPLETED_STATUS",
                "1-export_to_CSV.py"
                ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Write task data
        writer.writerows(todo_progress_data)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_progress_data = get_employee_todo_progress(employee_id)
    export_to_csv(employee_id, todo_progress_data)
