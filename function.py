#!/usr/bin/python
#coding=utf8
import itchat
import  time
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    print(msg)

    # 当消息不是由自己发出的时候
    return u"[我是管家小渣渣：本人暂时不在稍后会与你联系。]{}".format('aaaaaaaaaaaaaaaa')
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
