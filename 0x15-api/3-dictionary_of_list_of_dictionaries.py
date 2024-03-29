#!/usr/bin/python3
"""
Script to retrieve and display TODO list progress for a specific employee.

Usage: python3 script.py <employee_id>

This script fetches user information and their
TODO list from the JSONPlaceholder API,
calculates the progress, and displays completed tasks.

Author: Bruce Ambundo
"""
import json
import requests


def get_all_employees_todo_progress():
    """
    Fetches TODO list progress for all employees
    from the JSONPlaceholder API.

    Returns:
        dict: Dictionary containing task details for all employees.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"

    all_employees_data = {}

    # Fetch TODO progress for each employee
    for user_id in range(1, 11):  # Assuming 10 employees based on the example
        user_response = requests.get(f"{base_url}/{user_id}")
        user_data = user_response.json()

        todo_response = requests.get(f"{base_url}/{user_id}/todos")
        todo_data = todo_response.json()

        todo_progress_data = []
        for task in todo_data:
            task_data = {
                "username": user_data.get('username', 'Unknown'),
                "task": task.get('title', 'Untitled'),
                "completed": task.get('completed', False)
            }
            todo_progress_data.append(task_data)

            all_employees_data[str(user_id)] = todo_progress_data

    return all_employees_data


def export_to_json(todo_progress_data):
    """
    Exports TODO progress data for all
    employees to a JSON file.

    Args:
        todo_progress_data (dict): Dictionary 
        containing task details for all employees.

    Returns:
        None
    """
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as json_file:
        json.dump(todo_progress_data, json_file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    todo_progress_data = get_all_employees_todo_progress()
    export_to_json(todo_progress_data)
