#!/usr/bin/python
#coding=utf8
import itchat
import  time
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    return  u"[主人暂时不在，我是周小秘]{}".format(msg['Text'])
        # 回复给好友
if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2)#enablecmdqr参数是用于在命令行上生成二维码，用于linux服务器
    itchat.run(debug=True)