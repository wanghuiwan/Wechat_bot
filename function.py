#!/usr/bin/python
#coding=utf8
import itchat
# import pymysql
import requests
import  time
from random import choice
from itchat.content import *
KEY = '983eb78b67a046cd9b2f8c58b9751d8a'
from yuliao import a
from city_code2 import city_code2
import requests
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




@itchat.msg_register(TEXT)
def text_reply(msg):
    if msg['Content'] == 'help':
        data = '\nReply message:help  Show command help\n' \
               'Query weather：msg=天气深圳\n' \
               'Query Chinese English translation：msg=翻译i love you\n' \
               'Query intelligent chat：msg=你好\n' \
               'Query jokes：msg=笑话\n' \
               'Query lyrics⑴：msg=歌词后来\n' \
               'Query lyrics⑵：msg=歌词后来-刘若英\n' \
               'Query calculation⑴：msg=计算1+1*2/3-4\n' \
               'Query calculation⑵：msg=1+1*2/3-4\n' \
               'Query IP⑴：msg=归属127.0.0.1\n' \
               'Query IP⑵(Not supported at the moment)：msg=127.0.0.1\n' \
               'Query mobile phone⑴：msg=归属13430108888\n' \
               'Query mobile phone⑵：msg=13430108888\n' \
               'Idiom query：msg=成语一生一世\n' \
               'Query Wubi / Pinyin：msg=好字的五笔/拼音\n' \
               ''
        # '回复:xx市天气或者xx市xx区天气或者xx(市)天气  会回复该市当天天气\n' \
        # '例如: 北京市天气,北京天气,北京市朝阳区天气\n' \
        # '回复:XX是猪 回复你说的对，%s真的是猪^(*￣(oo)￣)^' \
        return u"[我是机器人小渣渣：]{}".format('%s' % data)
    try:
        aa = choice(a[msg['Content']])
        return aa
    except:
        msgs = qingyunkeApi(msg)
        return msgs
        # 当消息不是由自己发出的时候
        # return u"[我是机器人小渣渣：正在测试机器人]{}".format('.')
        # 回复给好友


@itchat.msg_register('Text',isGroupChat=True)
def text_reply(msg):
    msg = msg['Content']
    # 当回复是XXXX是猪时会回复信息.趣味.
    if msg[-2:] =='是猪':
        return u"[I'm a robot: little slag:]\n{}".format('你说的对，%s真的是猪^(*￣(oo)￣)^' % msg[:-2])
    # 如果结尾是天气的会根据规则截取并返回天气信息
    elif msg[-2:] =='天气':
        msg = msg[0:-2]
        try:
            city = msg.split('市')[0]
            qu = city
        except:
            city = msg.split('天气')[0]
            qu = city
        try:
            qu = msg.split('市')[1].split('区')[0]
            if qu =='':
                qu = city
        except:
            qu = city
        print(city + qu)
        try:
            msg= get_weather(city, qu)
        except:
            msg = "回复:xx市天气或者xx市xx区天气或者xx(市)天气  会回复该市当天天气\n"
        return msg
    # 增加青云客智能Api
    elif msg[:2]=='天气' or msg[:2] =='翻译' or msg[:2] =='笑话' or msg[:2] =='歌词' or msg[:2] =='计算' or msg[:2] =='归属'or msg[:2] =='成语' or msg[-5:] =='五笔/拼音':
        msgs = qingyunkeApi(msg)
        return msgs
    # 增加帮助指令.涵盖可以使用的命令
    elif msg=='help':
        data='\nReply message:XX是猪 回复你说的对，%s真的是猪^(*￣(oo)￣)^\n' \
               'Reply message:help  Show command help\n' \
               'Query weather：msg=天气深圳\n' \
               'Query Chinese English translation：msg=翻译i love you\n' \
               'Query intelligent chat(Not supported at the moment)：msg=你好\n' \
               'Query jokes：msg=笑话\n' \
               'Query lyrics⑴：msg=歌词后来\n' \
               'Query lyrics⑵：msg=歌词后来-刘若英\n' \
               'Query calculation⑴：msg=计算1+1*2/3-4\n' \
               'Query calculation⑵(Not supported at the moment)：msg=1+1*2/3-4\n' \
               'Query IP⑴：msg=归属127.0.0.1\n' \
               'Query IP⑵(Not supported at the moment)：msg=127.0.0.1\n' \
               'Query mobile phone⑴：msg=归属13430108888\n' \
               'Query mobile phone⑵(Not supported at the moment)：msg=13430108888\n' \
               'Idiom query：msg=成语一生一世\n' \
               'Query Wubi / Pinyin：msg=好字的五笔/拼音\n' \
               ''
            # '回复:已有指令 可以进行对答\n' \
            # '回复:xx市天气或者xx市xx区天气或者xx(市)天气  会回复该市当天天气\n' \
            # '例如: 北京市天气,北京天气,北京市朝阳区天气\n' \
        return u"[I'm a robot: little slag：]\n{}".format('%s' % data)
    else:
        try:
            aa = choice(a[msg])
            return aa
        except:
            # 当消息不是由自己发出的时候
            # return u"[我是渣男的机器人小渣渣：正在测试自动机器人]{}".format('.')
            # 回复给好友
            pass


def qingyunkeApi(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s'
    aaa = requests.get(url % msg)
    print(aaa.json())
    msgs = aaa.json()['content'].replace('{br}','\n')
    return msgs


def get_weather(city,qu):
    # 天气接口获取当天的天气信息
    url = 'http://t.weather.itboy.net/api/weather/city/%s'
    #获取地区code
    aa = city_code2[city][qu]['city_code']
    print(url % aa)
    aaa = requests.get(url % aa)
    msgs = aaa.json()
    msg = '本次数据更新时间为:' + msgs['cityInfo']['updateTime'] + '\n' + \
          ' 今天:' + msgs['data']['forecast'][0]['fx'] + msgs['data']['forecast'][0]['fl'] + msgs['data']['forecast'][0][
              'type'] + '\n' + \
          ' 今天最高气温:' + msgs['data']['forecast'][0]['high'] + '\n' + \
          ' 今天最低气温:' + msgs['data']['forecast'][0]['low'] + '\n' + \
          ' 日出时间为:' + msgs['data']['forecast'][0]['sunrise'] + '\n' + \
          ' 日落时间为:' + msgs['data']['forecast'][0]['sunset'] + '\n' + \
          ' PS:' + msgs['data']['forecast'][0]['notice'] + '\n'
    return msg

if __name__ == '__main__':
    #     #     itchat.auto_login(enableCmdQR=2)#enablecmdqr参数是用于在命令行上生成二维码，用于linux服务器
    #     itchat.auto_login(enableCmdQR=2)
    #     itchat.run(debug=True)
    itchat.auto_login(enableCmdQR=False)
    itchat.run(debug=True)