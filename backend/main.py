#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from os import path

from db_operations import EticaDB

from bottle import Bottle, route, run
from bottle import redirect, request

DB_NAME = path.abspath('broadbeams.db')

edb = EticaDB('sqlite', dbname=DB_NAME)
edb.create_db_tables()

app = Bottle()

@route('/')
@route('/users')
def list_users():
    users = 'users'
    output = edb.print_all_data(users)
    return output


@route('/add', method='GET')
def add_user():
    uid = request.query.uid
    privatetoken = request.query.privatetoken
    ip = request.query.ip
    port = request.query.port
    # status = True

    data = {'uid': uid, 'privatetoken': privatetoken, 'ip': ip, 'port': port}
    result = edb.add_new_user(data)
    return result


if __name__ == "__main__":
    run(host='127.0.0.1', port=8000, reloader=True, quiet=False, debug=True)
