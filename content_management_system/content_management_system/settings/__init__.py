import pymysql
pymysql.install_as_MySQLdb()

""" To set the database configuration as environment"""
from .local import *
# from .production import *
# from .development import *
# from .local import *