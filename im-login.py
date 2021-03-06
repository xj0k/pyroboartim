# -*- coding: utf-8 -*-

import sys
import PySimpleGUIQt as sg
import sleekxmpp

jid = "xj0k2@chatserver.space"
password = "1234!@#$"
server = ("chatserver.space", 5222)

gClient = sleekxmpp.ClientXMPP(jid, password)

def im_login():
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
    [sg.Button("start login",key='login')],
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


