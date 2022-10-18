#!/usr/bin/python3
# A script that gathers data from an API.
# Write a Python script that, using this REST API, for a given employee ID, returns information about his/her ToDo list progress

import requests
from sys import api_version, argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    emp_id = argv[1]
    total_todos = 0
    done_todos = 0
    done_todos_titles = []

    res = requests.get( API_URL + '/users/' + emp_id)
    emp_name = res.json().get('name', 'user name not found')

    tres = requests.get( API_URL + '/todos/' + emp_id)
    emp_todos = tres.json()

    for todo in emp_todos:
        total_todos += 1
        if todo.get('completed') is True:
            done_todos += 1
            done_todos_titles.append(todo.get(
                                          'title',
                                          'no title found'
                                          ))

    print('Employee {} is done with tasks({}/{}):'.format(
                                                   emp_name,
                                                   done_todos,
                                                   total_todos
                                                   ))

    for title in done_todos_titles:
        print('\t ' + title)

