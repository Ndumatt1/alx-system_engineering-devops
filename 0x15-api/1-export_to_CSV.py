#!/usr/bin/python3
''' This script export data in CSV format '''
import requests
from sys import argv

if __name__ == '__main__':
    ids = int(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(ids)

    todos = requests.get(todo_url).json()
    users = requests.get(user_url).json()

    todo_list = []
    for todo in todos:
        if todo['userId'] == ids:
            todo_list.append(todo)

    user_name = users['username']
    file = '{}.csv'.format(ids)
    with open(file, 'w') as csv_file:
        for data in todo_list:
            title = data.get('title')
            complete = data.get('completed')
            content = '"{ids}","{user_name}","{complete}","{title}"\n'
            csv_file.write(content)
