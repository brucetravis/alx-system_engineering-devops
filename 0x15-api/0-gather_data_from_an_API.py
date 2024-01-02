#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    
    # Fetch user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()
    
    # Calculate TODO progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)
    
    # Display information
    print(f"Employee {user_data.get('name', 'Unknown')} is done with tasks({completed_tasks}/{total_tasks}):")
    
    for task in todo_data:
        if task.get('completed', False):
            print(f"\t{task.get('title', 'Untitled')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
