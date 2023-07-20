#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        if employee_response.status_code == 200 and todos_response.status_code == 200:
            employee_data = employee_response.json()
            todos_data = todos_response.json()

            employee_name = employee_data["name"]
            total_tasks = len(todos_data)
            completed_tasks = [task for task in todos_data if task["completed"]]
            num_completed_tasks = len(completed_tasks)

            print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

            for task in completed_tasks:
                print(f"\t{task['title']}")

        else:
            print(f"Failed to fetch TODO list for employee {employee_id}. Error code: {employee_response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
    