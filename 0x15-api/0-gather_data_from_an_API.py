#!/usr/bin/python3
'''This module fetches data for a given employee ID and returns his/her TODO
list progress
'''
import requests
from sys import argv

if __name__ == '__main__':
    user_id = int(argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()
    total = 0
    task = 0
    completed_list = []
    user_name = users.get('name')

    for todo in todos:
        if todo.get("userId") == user_id:
            total += 1
            if todo.get("completed"):
                task += 1
                completed_list.append(todo)
    print('Employee {} is done with tasks({}/{}):'.format(
            user_name, task, total))
    for item in completed_list:
        print('\t {}'.format(item.get("title")))
