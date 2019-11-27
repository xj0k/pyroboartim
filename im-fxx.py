# -*- coding: utf-8 -*-

import sys
import PySimpleGUIQt as sg
import sleekxmpp


jids = [
    "xj0k2@chatserver.space",
    "tangjunbin@chatserver.space",
    "fengyijun@chatserver.space",
    "dengweiyi@chatserver.space"
    ]
passwords = [ "1234!@#$",'tangjunbin','fengyijun','dengweiyi' ]
acc = 0
jid = jids[acc]
password = passwords[acc]

server = ("chatserver.space", 5222)

gClient = sleekxmpp.ClientXMPP(jid, password)

def im_send(msg):
    mto = 'xj0k1234@trillian.im'
    print("开始发送:%s" % msg)
    gClient.send_message(mto,msg)

def recv_msg(msg):
    m = msg['body']
    print("received:%s" % m)

def im_login():
    gClient.add_event_handler('message',recv_msg)
    print("login with:%s" % jid)

    if gClient.connect(server):
        # 链接服务器
        print("链接成功，开始发送在线状态")
        # 发送在线状态
        gClient.send_presence()
        # 启动消息处理过程
        gClient.process(block=False)
        print("开始处理消息.")


def im_logout():
    gClient.disconnect(wait=True)


layout = [
    [sg.Text("Will start chat.")],
    [sg.InputText(key='message')],
    [sg.Button("请登录",key='login')],
    [sg.Button("send",key='send')],
    [sg.Button('exit',key='exit')]
]
window = sg.Window("chatting",layout)
while True:
    event,values = window.read()
    print(event,values)
    if event == 'exit' or event is None:
        im_logout()
        window.close()
        sys.exit(0)

    if event == 'login':
        print("Will start login.")
        im_login()

    if event == 'send':
        imsg=window.Element('message').Get()
        print(imsg)
        im_send(imsg)

