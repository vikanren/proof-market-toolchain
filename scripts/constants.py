import os

VERSION = open(os.path.dirname(os.path.abspath(__file__)) + "/../VERSION", "r").read()
URL = 'http://try.dbms.nil.foundation/'
DB_NAME = 'market2'
MOUNT = '/v' + VERSION.replace('.', '_')
