#!/usr/bin/python
#coding=utf8
from city_code2 import city_code2
import requests



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


def juhe_xingzuo(msg):
    url = 'http://web.juhe.cn/constellation/getAll?consName=%s&type=today&key=%s'
    aaa = requests.get(url % msg)
    print(aaa.json())
    msgs = aaa.json()['content'].replace('{br}','\n')
    return msgs


def tianxing(type):
    '''
    :param type:int #1表示早安 2表示定时任务 3表示晚安
    :param y:int
    :return: int
    '''
    if type ==1:
        #早安
        url = 'http://api.tianapi.com/zaoan/index'
    elif type ==3:
        #晚安
        url = 'http://api.tianapi.com/wanan/index'
    elif type ==2:
        # 朋友圈文案
        url = 'http://api.tianapi.com/pyqwenan/index'
    else:
        # 每日一句美好英语
        url = 'http://api.tianapi.com/everyday/index'
    params = {'key': '4c1c67d037a124a623b829bb990a7b64'}
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = requests.get(url, params=params, headers=headers)
    data = data.json()
    print(data)
    if type == 1 or type == 2 or type == 3:
        return {"types":"txt","msg" : data['newslist'][0]['content']}
    else :
        return {"types":"img","msg1" : data['newslist'][0]['imgurl'],"msg2":data['newslist'][0]['content'],"msg3":data['newslist'][0]['note']}
