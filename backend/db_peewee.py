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
    user_id = IntegerField(primary_key=True)
    uid = TextField(unique=True)
    private_token = TextField()
    status = BooleanField(default='1')

    class Meta:
        db_table = USERS


class Addresses(Base):
    address_id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(Users, to_field='user_id', related_name='users', unique=True)
    ip = TextField()
    port = TextField()
    timestamp = DateTimeField(default=datetime.utcnow())

    class Meta:
        db_table = ADDRESSES


def create_tables():
    with database:
        database.create_tables([Users, Addresses])


def add_user(data=''):
    if data == '' : return

    try:
        user = Users.create(
            uid=data['uid'],
            private_token=data['private_token']
        )
    except IntegrityError as e:
        return print(str(e))
    else:
        return print('id:', user, data)


def add_address(data=''):
    if data == '' : return

    address = Addresses.insert(
        user_id=Users.select(Users.user_id).where(Users.uid == data['uid']).exists(),
        ip=data['ip'],
        port=data['port']
    ).on_conflict('replace').execute()

    return print('address_id:', address, data)


def search_user(uid):
    if uid == '' : return

    


def delete_user(data=''):
    if data == '' : return

    user_id = Users.select(Users.user_id).where(Users.uid == data['uid'])

    erase_address = Addresses.delete().where(Addresses.user_id == user_id).execute()
    erase_user = Users.delete().where(Users.uid == data['uid']).execute()

    return print(erase_user, erase_address)


def clear_addresses():
    if data == '' : return

    query = Addresses.select(Addresses.user_id)\
        .join(Users, on=(Addresses.user_id == Users.user_id))\
        .where(Users.user_id == None)

    count = 0
    for q in query:
        Addresses.delete().where(Addresses.user_id == q).execute()
        count += 1

    return print(f'Removed {count} records.')


def show_all():
    users = Users.select()
    address = Addresses.select()


if __name__ == '__main__':
    create_tables()

    data = {'uid': 'test', 'private_token': 'private', 'ip': '127.0.0.2', 'port': '8080'}
    add_user(data)
    add_address(data)
    delete_user(data)
    clear_addresses()
