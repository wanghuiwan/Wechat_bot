#!/usr/bin/python
# coding:utf-8
# pythonproject - conn_mysql.py
# 2021/11/11 16:38

__author__ = 'Martin Wang <357951@qq.com>'

import pymysql
import sqlite3
from time import sleep

db_host = "47.91.228.122"
db_name = "yuliaoku"
db_user = "root"
db_pass = "123456"
db_port = 3306

# Creating a database with tables if not exists.
# db = pymysql.connect(host=db_host, database=db_name, user=db_user, password=db_pass, port=db_port, charset='utf8')
# curs = db.cursor()
# curs.execute(
#     'CREATE TABLE IF NOT EXISTS Chats (chat_id	bigint NOT NULL UNIQUE,rules	TEXT ,rank_delay	INTEGER NOT NULL DEFAULT 900,ranking_delay	INTEGER NOT NULL DEFAULT 1800,admins_delay	INTEGER NOT NULL DEFAULT 3600,rankuser_delay	INTEGER NOT NULL DEFAULT 120,    ranking_time	bigint DEFAULT 1,admins_time   bigint DEFAULT 1,rank_on INTEGER NOT NULL DEFAULT 1,PRIMARY KEY(chat_id))')
# # Users Table
# curs.execute(
#     """CREATE TABLE IF NOT EXISTS Users (chat_id	bigint NOT NULL,user_id	bigint NOT NULL,username	TEXT,firstname	TEXT,user_level	INTEGER,experience	INTEGER,start_exp	INTEGER,warnings	INTEGER,exp_time	bigint,command_time	bigint,rank_time	bigint DEFAULT 1,rankuser_time	bigint DEFAULT 1,is_admin boolean DEFAULT FALSE,PRIMARY KEY(chat_id,user_id),FOREIGN KEY(chat_id) REFERENCES Chats(chat_id) ON DELETE CASCADE)""")
#
# # 记录存储的命令用于自动回复
# curs.execute(
#     """CREATE TABLE IF NOT EXISTS Commands (chat_id       bigint NOT NULL,user_id bigint NOT NULL,username        TEXT,command  TEXT,command_time     bigint,command_data   TEXT)""")
#
# # 记录定时信息发送
# curs.execute(
#     """CREATE TABLE IF NOT EXISTS timing_message (chat_id       bigint NOT NULL,user_id bigint NOT NULL,timing  int,message   VARCHAR(100), message_data  TEXT ,state INT , UNIQUE KEY `chat_id_message` (`chat_id`,`message`))""")
#
# # 报价
# curs.execute(
#     """CREATE TABLE IF NOT EXISTS change_money (chat_id       bigint NOT NULL,user_id bigint NOT NULL,message_data  TEXT ,create_date DATE )""")

# db.commit()
# db.close()

def select_query(database, column, table, column_name=None, column_value=None, column_name2=None, column_value2=None):
    """
    :param database: Sqlite3 database
    :param column: a string of the selected column to get info from ( to get all columns, string should be "all").
    :param table: From which table
    :param column_name: a string of the column you want to equal to a value ( username = )
    :param column_value: the value of the column_name ( column_name = "drake")
    :param column_name2: a string Optional - adds AND option to the query to check with another column
    :param column_value2: Optional the value of column_name2
    :return: None or results
    """
    column_values = column_value
    if type(column_value) == str:
        column_value = "'{}'".format(column_value)
    if type(column_value2) == str:
        column_value2 = "'{}'".format(column_value2)
    cursor = database.cursor()
    if column.lower() == "all" and column_name2 is not None and column_value2 is not None:
        cursor.execute("SELECT * FROM {} WHERE {} = {} AND {} = {}"
                       .format(table, column_name, column_value, column_name2, column_value2))
        return cursor.fetchone()
    elif column.lower() == "all" and column_name2 is None and column_value2 is None:
        cursor.execute("SELECT * FROM {} WHERE {} = {}"
                       .format(table, column_name, column_value))
        return cursor.fetchone()
    elif column.lower() == "alls" and column_name2 is None and column_value2 is None:
        cursor.execute("SELECT * FROM {} WHERE {} = {}"
                       .format(table, column_name, column_value))
        return cursor.fetchall()
    elif column.lower() == "alls" and column_name2 is not None and column_value2 is not None:
        cursor.execute("SELECT * FROM {} WHERE {} = {} AND {} = {}"
                       .format(table, column_name, column_value, column_name2, column_value2))
        return cursor.fetchall()
    elif column_name2 is None and column_value2 is None:
        cursor.execute("SELECT {} FROM {} WHERE {} = {}"
                       .format(column, table, column_name, column_value))
        return cursor.fetchone()
    elif column_value2 is None:
        cursor.execute("SELECT {},{},{},{} FROM {} "
                       .format(column, column_name, column_values, column_name2, table))
        return cursor.fetchall()
    else:
        cursor.execute("SELECT {} FROM {} WHERE {} = {} AND {} = {}"
                       .format(column, table, column_name, column_value, column_name2, column_value2))
        return cursor.fetchone()



# checks if need to update the database every message
def update_data(database, chat_id, user_id, message, is_admin):
    user = message.from_user
    cursor = database.cursor()
    current_firstname = user.first_name
    current_firstname = current_firstname.replace("'", "")
    current_firstname = current_firstname.replace("", " ")
    # checking if the chat is already in the database
    result = select_query(database, "all", "Chats", "chat_id", chat_id)
    if result is None:
        default_rule = "'There are no rules yet, please contact an admin to set them.'"
        # in case the chat is not inside, adding the chat
        sql = "INSERT INTO Chats(chat_id, Rules, Rank_delay, Admins_delay, RankUser_delay," \
              "Ranking_delay, Ranking_time, Admins_time, Rank_on) VALUES({},{},{},{},{},{},{},{},{})" \
            .format(chat_id, default_rule, 900, 1800, 3600, 900, 1, 1, 1)
        print(sql)
        cursor.execute(sql)
        database.commit()

    # checking if the user is already in the database in the current chat.
    result = select_query(database, "user_id", "Users", "user_id", user_id, "chat_id", chat_id)
    if result is None:
        if not user.is_bot:
            sql = "INSERT INTO Users(chat_id, user_id, Username," \
                  "Firstname ,user_level, Experience, Start_exp, Warnings," \
                  " Exp_time, Command_time, Rank_time, RankUser_time, is_admin) " \
                  "VALUES({},{},'{}','{}',{},{},{},{},{},{},{},{},{})" \
                .format(chat_id, user.id, user.username, current_firstname, 2, 0, 0, 0, 0, 0, 0, 0, is_admin)
            print(sql)
            cursor.execute(sql)
            database.commit()
    else:
        current_username = user.username
        username = select_query(database, "Username", "Users", "user_id", user_id, "chat_id", chat_id)[0]
        firstname = select_query(database, "Firstname", "Users", "user_id", user_id, "chat_id", chat_id)[0]
        if current_username != username:
            cursor.execute("UPDATE Users SET Username = '{}' WHERE chat_id = {} AND user_id = {}"
                           .format(current_username, chat_id, user_id))
        if current_firstname != firstname:
            cursor.execute("UPDATE Users SET Firstname = '{}' WHERE chat_id = {} AND user_id = {}"
                           .format(current_firstname, chat_id, user_id))
        cursor.execute("UPDATE Users SET is_admin = {} WHERE chat_id = {} AND user_id = {}"
                       .format(is_admin, chat_id, user_id))

        database.commit()
