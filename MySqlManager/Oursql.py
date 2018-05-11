#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from mysql.connector import Error
import config


def insert_project(project):
    query = "insert into t_project(c_project) values(%s)"

    args = (project,)

    db_config = config.datasourse

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def clear_sampling_result():
    query = "delete from  sampling_result"

    db_config = config.datasourse

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_sampling_result(result=[]):
    result = list(result)
    for i in result:
        query = "insert into t_sampling_result(result_value) values(%s)"

        args = (float(i))
        id = id + 1
        db_config = config.datasourse

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    insert_project('模型1')