#!/usr/bin/python3
''' This module exports data in JSON format '''

import json
import requests
import sys

if __name__ == '__main__':
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    todos = requests.get(todo_url).json()
    users = requests.get(users_url).json()

    todo_list = []
    for todo in todos:
        if todo['userId'] == user_id:
            todo_list.append(todo)
    user_name = users["username"]
    tasks_list = []
    for task in todo_list:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = user_name
        tasks_list.append(task_dict)
    content = {}
    key = '{}'.format(user_id)
    content[key] = tasks_list
    file = '{}.json'.format(str(user_id))
    with open(file, 'w') as json_file:
        json.dump(content, json_file)
