import pymysql.cursors
import logging
import os

'''
    This file includes all helper functions
'''


def connect_db():
    # connect to db
    connection = pymysql.connect(host=os.getenv("MYSQL_HOST"),
                                 port=int(os.getenv("MYSQL_PORT")),
                                 user=os.getenv("MYSQL_USERNAME"),
                                 password=os.getenv("MYSQL_PASSWORD"),
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def log():
    # set up logging for the app
    logging.basicConfig(level=logging.INFO, filemode='a')

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('successgy.log')
    formatter = logging.Formatter(
        "[%(asctime)s] - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
