from sqlalchemy import create_engine
from config import *


target_database = 'mysql+pymysql://%s:%s@%s:%s' % (DB_USERNAME, DB_PASSWORD, DB_HOSTNAME, DB_PORT)
# http://docs.sqlalchemy.org/en/rel_0_9/dialects/mysql.html#dialect-mysql-pymysql-connect

engine = create_engine(target_database, echo=True)
# connect to server
# echo = True means show detail sqlalchemy operation

engine.execute("CREATE DATABASE %s" % DB_DATABASE)
# create db

engine.execute("USE %s" % DB_DATABASE)
# select new db
