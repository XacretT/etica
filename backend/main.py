#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from db_operations import EticaDB

from bottle import Bottle, route, run
from bottle import redirect, request

DB_NAME = 'broadbeams.db'

edb = EticaDB('sqlite', dbname=DB_NAME)
edb.create_db_tables()

app = Bottle()

@route('/')
@route('/users')
def list_users():
    users = 'users'
    output = edb.print_all_data(users)
    return output


@route('/add/<uuid>')
def add_user(uuid):
    query = f'INSERT INTO users(uuid) VALUES ({uuid});'
    result = edb.execute_query(query)
    return result

if __name__ == "__main__":
   run(host='127.0.0.1', port=8000, reloader=True, quiet=False, debug=True)

