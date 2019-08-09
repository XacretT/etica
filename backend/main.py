#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from db_peewee import *

from bottle import Bottle, route, run
from bottle import redirect, request
from bottle import template

create_tables()
app = Bottle()


@route('/')
@route('/users')
def list_users():
    output = template('templates/list.tpl', rows=show_all())
    return output


@route('/add', method='GET')
def add_user():
    uid = request.query.uid
    branch = request.query.branch
    ip = request.query.ip
    port = request.query.port

    data = {'uid': uid,
            'branch': branch,
            'ip': ip,
            'port': port}

    return add_new_user(data)


if __name__ == "__main__":
    run(host='127.0.0.1', port=8000, reloader=True, quiet=False, debug=True)
