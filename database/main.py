import pymysql.cursors
from contextlib import closing
import json
from config import DB_CONFIG
from pprint import pprint


def get_connection():
    connection = pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database'],
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


users_table_name = 'robocontest_bot_users'
attempts_table_name = 'robocontest_bot_attempts'


def get_user_attempt(attempt_id):
    with closing(get_connection()) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM testdb.{attempts_table_name} WHERE attempt_id = %s', attempt_id)
            record = cursor.fetchone()

    return record


def update_attempt_status(attempt_id, status):
    with closing(get_connection()) as connection:
        with connection.cursor() as cursor:
            sql = f'UPDATE testdb.{attempts_table_name} SET status = %s WHERE attempt_id = %s'
            cursor.execute(sql, (status, attempt_id))
            connection.commit()

    return_value = 'not updated'

    if connection.affected_rows() != 0:
        return_value = 'updated'

    return return_value
