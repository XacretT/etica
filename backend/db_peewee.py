#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime
from hashlib import sha256


DATABASE = 'test.db'  # ':memory:'

USERS = 'users'
ADDRESSES = 'addresses'
ALIASES = 'aliases'
CONTROL = 'control'

database = SqliteDatabase(DATABASE)


class Base(Model):
    class Meta:
        database = database


class Users(Base):
    id = IntegerField(primary_key=True)
    public = TextField()
    prev_hash = TextField(null=True)
    curr_hash = TextField(null=False)

    class Meta:
        db_table = USERS


class Addresses(Base):
    # id = IntegerField(primary_key=True)
    public = ForeignKeyField(Users, backref='ip_ports')
    ip = TextField(null=False)
    port = TextField(null=False)

    class Meta:
        db_table = ADDRESSES


class Aliases(Base):
    # id = IdentityField(primary_key=True)
    public = ForeignKeyField(Users, backref='aliases')
    alias = TextField(null=False, unique=True)

    class Meta:
        db_table = ALIASES


class Control(Base):
    # id = IdentityField(primary_key=True)
    public = ForeignKeyField(Users, backref='controls')
    status = BooleanField(default='1')

    class Meta:
        db_table = CONTROL


def create_tables():
    with database:
        database.create_tables([Users, Addresses, Aliases, Control])

#
def add_user(data=''):
    if data == '' : return

    user_id = (Users
               .select()
               .count())
    public = data
    prev_hash = (Users
                 .select(Users.curr_hash)
                 .where(Users.id == user_id))

    phrase = (f'{public}{prev_hash}')

    curr_hash = (sha256(phrase.encode())
                 .hexdigest())
    user = (Users
            .create(public=public,
                    prev_hash=prev_hash,
                    curr_hash=curr_hash))

#
#
# def add_address(data=''):
#     if data == '' : return
#
#     user_id = (Users
#                .select(Users.user_id)
#                .where(Users.uid == data['uid']))
#
#     address = (Addresses
#                .insert(user_id=user_id,
#                        ip=data['ip'],
#                        port=data['port'])
#                .on_conflict('replace')
#                .execute())
#
#     return print('address_id:', address, data)
#
#
# def add_new_user(data=''):
#     if data == ''  : return
#
#     result = ''
#     result += add_user()
#     result += add_address()
#
#     return result
#
# def search_user(uid=''):
#     if uid == '' : return
#
#     query = (Addresses
#              .select(Addresses.ip, Addresses.port)
#              .join(Users)
#              .where(Users.uid == uid))
#
#     for address in query:
#         return address.ip, address.port
#
#
# def delete_user(data=''):
#     if data == '' : return
#
#     user_id = (Users
#                .select(Users.user_id)
#                .where(Users.uid == data['uid']))
#
#     erase_address = (Addresses
#                      .delete()
#                      .where(Addresses.user_id == user_id)
#                      .execute())
#
#     erase_user = (Users
#                   .delete()
#                   .where(Users.uid == data['uid'])
#                   .execute())
#
#     return print(erase_user, erase_address)
#
#
# def clear_addresses():
#     query = (Addresses
#              .select(Addresses.user_id)
#              .join(Users, on=(Addresses.user_id == Users.user_id))
#              .where(Users.user_id == None))
#
#     count = 0
#     for q in query:
#         _clear = (Addresses
#                   .delete()
#                   .where(Addresses.user_id == q))
#
#         _clear.execute()
#         count += 1
#
#     return print(f'Removed {count} records.')
#
#
# def show_all():
#     query = (Users
#              .select(Users.user_id,
#                      Users.uid,
#                      Users.status,
#                      Addresses.ip,
#                      Addresses.port,
#                      Addresses.timestamp)
#              .join(Addresses))
#
#     raws = []
#     for raw in query:
#         raws.append([str(raw.user_id),
#                      raw.uid,
#                      raw.addresses.ip,
#                      raw.addresses.port,
#                      str(raw.addresses.timestamp),
#                      str(raw.status)])
#     return raws


if __name__ == '__main__':
    create_tables()

    # Users.create(public='first_user',
    #              prev_hash='NeTy',
    #              curr_hash=sha256((f'first_userNeTy').encode()).hexdigest())
    print(sha256((f'first_userNeTy').encode()).hexdigest())
    add_user('second_user')

    query = Users.select().tuples()
    for o1, o2, o3, o4 in query:
        print(f'{o1}\t{o2}\t{o3}\t{o4}')
