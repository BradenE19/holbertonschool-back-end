#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_todo_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(employee_todo_url)

    if response.status_code == 200:
        todos = response.json()
        completed_todos = [todo for todo in todos if todo["completed"]]
        total_todos = len(todos)
        completed_todos_count = len(completed_todos)

        progress_percentage = (completed_todos_count / total_todos) * 100

        return {
            "total_todos": total_todos,
            "completed_todos_count": completed_todos_count,
            "progress_percentage": progress_percentage
        }
    else:
        print(f"Failed to fetch TODO list for employee {employee_id}. Error code: {response.status_code}")
        return None

if __name__ == "__main__":
    employee_id = 1  # Replace this with the employee ID you want to query
    employee_progress = get_employee_todo_progress(employee_id)

    if employee_progress:
        print(f"Employee {employee_id} TODO List Progress:")
        print(f"Total Todos: {employee_progress['total_todos']}")
        print(f"Completed Todos: {employee_progress['completed_todos_count']}")
        print(f"Progress Percentage: {employee_progress['progress_percentage']}%")

