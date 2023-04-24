#!/usr/bin/python3
'''This module fetches data for a given employee ID and returns his/her TODO
list progress
'''
import requests
from sys import argv

if __name__ == '__main__':
    ids = int(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(ids)
    todos = requests.get(todo_url).json()
    users = requests.get(users_url).json()
    user_todo = []
    for todo in todos:
        if todo['userId'] == ids:
            user_todo.append(todo)
    total_task = len(user_todo)
    task_done = sum(todo['completed'] for todo in user_todo)

    print('Employee {} is done with tasks({}/{})'
          .format(users['name'], task_done, total_task))
    completed_todos = filter(lambda todo: todo['completed'], user_todo)
    for title in completed_todos:
        print('\t {}'.format(title['title']))
