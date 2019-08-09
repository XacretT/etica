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
    branch = TextField(unique=True)
    banned = BooleanField(default='1')

    class Meta:
        db_table = USERS


class Addresses(Base):
    address_id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(Users,
                              to_field='user_id',
                              related_name='users',
                              unique=True)
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
        user = (Users
                .create(uid=data['uid'],
                        branch=data['branch']))

    except IntegrityError as e:
        return print(str(e))
    else:
        return print('id:', user, data)


def add_address(data=''):
    if data == '' : return

    user_id = (Users
               .select(Users.user_id)
               .where(Users.uid == data['uid']))

    address = (Addresses
               .insert(user_id=user_id,
                       ip=data['ip'],
                       port=data['port'])
               .on_conflict('replace')
               .execute())

    return print('address_id:', address, data)


def add_new_user(data=''):
    if data == ''  : return

    result = ''
    result += add_user()
    result += add_address()

    return result

def search_user(uid=''):
    if uid == '' : return

    query = (Addresses
             .select(Addresses.ip, Addresses.port)
             .join(Users)
             .where(Users.uid == uid))

    for address in query:
        return address.ip, address.port


def delete_user(data=''):
    if data == '' : return

    user_id = (Users
               .select(Users.user_id)
               .where(Users.uid == data['uid']))

    erase_address = (Addresses
                     .delete()
                     .where(Addresses.user_id == user_id)
                     .execute())

    erase_user = (Users
                  .delete()
                  .where(Users.uid == data['uid'])
                  .execute())

    return print(erase_user, erase_address)


def clear_addresses():
    query = (Addresses
             .select(Addresses.user_id)
             .join(Users, on=(Addresses.user_id == Users.user_id))
             .where(Users.user_id == None))

    count = 0
    for q in query:
        _clear = (Addresses
                  .delete()
                  .where(Addresses.user_id == q))

        _clear.execute()
        count += 1

    return print(f'Removed {count} records.')


def show_all():
    query = (Users
             .select(Users.user_id,
                     Users.uid,
                     Users.status,
                     Addresses.ip,
                     Addresses.port,
                     Addresses.timestamp)
             .join(Addresses))

    raws = []
    for raw in query:
        raws.append([str(raw.user_id),
                     raw.uid,
                     raw.addresses.ip,
                     raw.addresses.port,
                     str(raw.addresses.timestamp),
                     str(raw.status)])
    return raws


if __name__ == '__main__':
    create_tables()

    data = {'uid': 'test3', 'private_token': 'private', 'ip': '127.0.0.4', 'port': '8080'}
    #add_user(data)
    #add_address(data)
    # print(search_user('test'))
    print(show_all())
    # delete_user(data)
    # show_all()
    #clear_addresses()
