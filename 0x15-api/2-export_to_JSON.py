#!/usr/bin/python3


import requests
import sys
import json

def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from the JSONPlaceholder API.

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
            "task": task.get('title', 'Untitled'),
            "completed": task.get('completed', False),
            "username": user_data.get('username', 'Unknown')
        }
        todo_progress_data.append(task_data)
    
    return {str(employee_id): todo_progress_data}

def export_to_json(employee_id, todo_progress_data):
    """
    Exports employee TODO progress data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        todo_progress_data (dict): Dictionary containing task details.

    Returns:
        None
    """
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as json_file:
        json.dump(todo_progress_data, json_file)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_progress_data = get_employee_todo_progress(employee_id)
    export_to_json(employee_id, todo_progress_data)
