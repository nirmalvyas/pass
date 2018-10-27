import os
import pymongo
from pymongo import MongoClient
import socket

client = MongoClient(host='0.0.0.0', port=27017)

MONGODB_HOST = '0.0.0.0'
MONGODB_PORT = 27017
MONGO_DB = 'test'

REDISHOST = 'localhost'
REDISPORT = '6379'
REDISPWD = ""
DB_HOST = 'localhost'
DB_PORT = '5432'
APP_NAME = 'production'
DB_USER = 'postgres'
DB_PASSWORD = ''

staging = False

host_name = socket.gethostname()

cwd = os.getcwd()

# SENTRY

DEBUG = True


SERVER_NAME = '127.0.0.1'
SERVER_PORT = 5000
DB_CONNECTION = "host='{0}' port='{1}' dbname='{2}' user='{3}' password='{4}'".format(DB_HOST, DB_PORT, APP_NAME, DB_USER, DB_PASSWORD)
SQLALCHEMY_DATABASE_URI = 'postgresql://' + str(DB_USER) + ':' \
                          + str(DB_PASSWORD) + '@' + str(DB_HOST) + \
                          ":" + str(DB_PORT) + '/' + str(APP_NAME)

