#!/usr/bin/python
#coding=utf8
import itchat
# import pymysql
import requests
import  time
from random import choice
KEY = '983eb78b67a046cd9b2f8c58b9751d8a'
from yuliao import a
# db_host = "47.91.228.122"
# db_name = "bot"
# db_user = "root"
# db_pass = "ABcd#1234"
# db_port = 3306

# # Creating a database with tables if not exists.
# db = pymysql.connect(host=db_host, database=db_name, user=db_user, password=db_pass, port=db_port)
# curs = db.cursor()
# curs.execute(
#     'CREATE TABLE IF NOT EXISTS Chats (chat_id	bigint NOT NULL UNIQUE,rules	TEXT ,rank_delay	INTEGER NOT NULL DEFAULT 900,ranking_delay	INTEGER NOT NULL DEFAULT 1800,admins_delay	INTEGER NOT NULL DEFAULT 3600,rankuser_delay	INTEGER NOT NULL DEFAULT 120,    ranking_time	bigint DEFAULT 1,admins_time   bigint DEFAULT 1,rank_on INTEGER NOT NULL DEFAULT 1,PRIMARY KEY(chat_id))')
# # Users Table
# curs.execute("""CREATE TABLE IF NOT EXISTS Users (chat_id	bigint NOT NULL,user_id	bigint NOT NULL,username	TEXT,firstname	TEXT,user_level	INTEGER,experience	INTEGER,start_exp	INTEGER,warnings	INTEGER,exp_time	bigint,command_time	bigint,rank_time	bigint DEFAULT 1,rankuser_time	bigint DEFAULT 1,is_admin boolean DEFAULT FALSE,PRIMARY KEY(chat_id,user_id),FOREIGN KEY(chat_id) REFERENCES Chats(chat_id) ON DELETE CASCADE)""")
#
#
# # 记录存储的命令用于自动回复
# curs.execute("""CREATE TABLE IF NOT EXISTS Commands (chat_id       bigint NOT NULL,user_id bigint NOT NULL,username        TEXT,command  TEXT,command_time     bigint,command_data   TEXT)""")
#
# # 记录定时信息发送
# curs.execute("""CREATE TABLE IF NOT EXISTS timing_message (chat_id       bigint NOT NULL,user_id bigint NOT NULL,timing  int,message   VARCHAR(100), message_data  TEXT ,state INT , UNIQUE KEY `chat_id_message` (`chat_id`,`message`))""")
# db.commit()
# db.close()
# # 自动回复
# # 封装好的装饰器，当接收到的消息是Text，即文字消息

# KEY = '983eb78b67a046cd9b2f8c58b9751d8a'

# def get_response(msg):
#     apiUrl = 'http://www.tuling123.com/openapi/api'
#     data = {
#         'key'    : KEY,
#         'info'   : msg,
#         'userid' : 'wechat-robot',
#     }
#     try:
#         r = requests.post(apiUrl, data=data).json()
#         return r.get('text')
#     except:
#         return

@itchat.msg_register('Text')
def text_reply(msg):
    try:
        aa = choice(a[msg['Content']])
        return aa
    except:
        # 当消息不是由自己发出的时候
        return u"[我是渣男的机器人小渣渣：正在测试自动机器人]{}".format('.')
        # 回复给好友


@itchat.msg_register('Text',isGroupChat=True)
def text_reply(msg):
    if msg['Content'][-2:] =='是猪':
        print(msg['Content'])
        # 当消息不是由自己发出的时候
        return u"[我是机器人小渣渣：]{}".format('你说的对，%s真的是猪^(*￣(oo)￣)^' % msg['Content'][:-2])

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2)#enablecmdqr参数是用于在命令行上生成二维码，用于linux服务器
    itchat.run(debug=True)
