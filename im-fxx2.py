# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
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

jid = 'xj0k1234@trillian.im'
password = '1234!@#$'
server = ("impp.trillian.im",3158)

gClient = sleekxmpp.ClientXMPP(jid, password)

def im_send(msg):
    mto = 'xj0k1234@trillian.im'
    print("开始发送:%s" % msg)
    gClient.send_message(mto,msg)
    r = window.Element('msg_display')
    m = '\n' +msg
    r.Update(value=m,append=True)

def recv_msg(msg):
    m = msg['body']
    print("received:%s" % m)
    r = window.Element('msg_display')
    m = '\n' + m
    r.Update(value=m,append=True)

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


layout2 = [
    [sg.Text("Will start chat.")],
    [sg.Button("登录",key='login')],
    [sg.Button("send",key='send')],
    [sg.Button('exit',key='exit')]
]

l_login = [
    [sg.Text("Will start chat.")],
    [sg.Button("登录", key='login'), sg.Button('exit', key='exit')]
]
l_chat = [
    [sg.Multiline(key='msg_display')],
    [sg.InputText(key='msg_send'), sg.Button("send", key='send')],
]

layout3 = [
   [ sg.Frame('login',key='win_login',layout=l_login,visible=True),
     sg.Frame('chat',key='win_chat',layout=l_chat,visible=False)]
]

window = sg.Window("chatting",layout3)
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
        window.Element('win_login').Update(visible=False)
        window.Element('win_chat').Update(visible=True)

    if event == 'send':
        imsg = values['msg_send']
        print(imsg)
        im_send(imsg)

