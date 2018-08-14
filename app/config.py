from os import environ
from sqlalchemy import create_engine
import psycopg2 as dbapi2
import logging


def get_database_informations():
    vars = ['DBNAME', 'DBUSER', 'DBPASS', 'DBHOST']

    for i in vars:
        if environ.get(i) is None:
            logging.error('Environment variable %s is not set' % i)
            return False

    dbdict = {
        'dbname': environ.get('DBNAME'),
        'dbuser': environ.get('DBUSER'),
        'dbpass': environ.get('DBPASS'),
        'dbhost': environ.get('DBHOST')
    }

    return dbdict


def get_db_connect():
    db_dict = get_database_informations()
    db_link = "postgresql://%s:%s@%s/%s" % (db_dict['dbuser'], db_dict['dbpass'], db_dict['dbhost'], db_dict['dbname'])
    return create_engine(db_link)
