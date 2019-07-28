#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime

DATABASE = 'test.db'  # ':memory:'
USERS = 'users'
ADDRESSES = 'addresses'

database = SqliteDatabase(DATABASE)


class Base(Model):
    class Meta:
        database = database


class Users(Base):
    id = IntegerField(primary_key=True)
    uid = TextField()
    private_token = TextField()
    status = BooleanField(default='1')

    class Meta:
        db_table = USERS


class Addresses(Base):
    id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(Users, related_name='id')
    ip = TextField()
    port = TextField()
    timestamp = DateTimeField(default=datetime.utcnow())

    class Meta:
        db_table = ADDRESSES


def create_tables():
    with database:
        database.create_tables([Users, Addresses])


def create_user(data):
    if data == '' : return

    Users.create(
        uid=data['uid'],
        private_token=data['private_token']
    )

    Addresses.create(
        user_id=Users.select(Users.id).where(Users.uid == data['uid']),
        # uid=data['uid'],
        ip=data['ip'],
        port=data['port']
    )

    return print(data)


def show_all():
    Users.select()
    Addresses.select()


if __name__ == '__main__':
    create_tables()
    private = 'private'
    test = Addresses.create(ip='127.0.0.1', port='2323')

    data = {'uid': 'test', 'private_token': 'private', 'ip': '127.0.0.2', 'port': '8080'}
    create_user(data)

    show_all()

    print("I'm sorry but not now.")