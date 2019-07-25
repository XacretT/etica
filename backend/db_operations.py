#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, MetaData, ForeignKey

from sqlalchemy.exc import IntegrityError

# Global Variables
SQLITE = 'sqlite'

# Table Names
USERS = 'users'
ADDRESSES = 'addresses'
STATUS = 'status'

class EticaDB:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")


    def create_db_tables(self):
        metadata = MetaData()
        users    = Table(USERS, metadata,
                         Column('id', Integer, primary_key=True),
                         Column('uuid', String, nullable=False, unique=True)
                         )
        address  = Table(ADDRESSES, metadata,
                         Column('id', Integer, primary_key=True),
                         Column('user_id', None, ForeignKey('users.id')),
                         Column('ip', String, nullable=False),
                         Column('port', String, nullable=False),
                         Column('ttl', String, nullable=False),
                         Column('join_date', DateTime, nullable=False)
                         )
        status   = Table(STATUS, metadata,
                         Column('id', Integer, primary_key=True),
                         Column('user_id', None, ForeignKey('users.id')),
                         Column('status', Boolean, nullable=False)
                         )
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)


    def execute_query(self, query=''):
        if query == '' : return
        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                my_string = ''
                for row in result:
                    # print(row)  # print(row[0], row[1], row[2])
                    my_string += str(row) + '\n'
                result.close()
                return my_string
        print("\n")

    def erase_all_data(self, table=''):
        query = f'DELETE FROM {table}'
        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)
            else:
                print(f'All data from "{table}" has been removed.')


if __name__ == '__main__':
    dbms = EticaDB(SQLITE, dbname='test.sqlite')
    dbms.create_db_tables()
    dbms.print_all_data('users')
    # dbms.execute_query('INSERT INTO users(uuid) VALUES ("first");')
    # dbms.execute_query('INSERT INTO users(uuid) VALUES ("second");')
    # dbms.execute_query('INSERT INTO users(uuid) VALUES ("old");')
    dbms.execute_query('SELECT * FROM "users";')
