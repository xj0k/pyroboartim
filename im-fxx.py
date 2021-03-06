# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
import sleekxmpp


# 用户名和密码
jid = "dengweiyi@chatserver.space"
password = 'dengweiyi'

# 服务器地址
server = ("chatserver.space", 5222)

# 初始化
gClient = sleekxmpp.ClientXMPP(jid, password)

def im_send(msg):
    mto = 'xj0k1234@trillian.im'
    mto='fengyijun@chatserver.space'
    print("开始发送:%s" % msg)
    gClient.send_message(mto,msg)

def recv_msg(msg):
    m = msg['body']
    print("接收到消息，内容是:%s" % m)
    r = window.Element('msg_display')
    r.Update(value=m + '\n', append=True)


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


layout_old = [
    [sg.Text("请登录.")],
    [sg.Image("logo-srap.png")],
    [sg.InputText(key='msg_display')],
    [sg.InputText(key='msg_send')],
    [sg.Button("send", key='send')],
    [sg.Button("登录", key='login')],
]

layout_login = [
    [sg.Text("请登录.")],
    [sg.Image("logo-srap.png")],
    [sg.Button("登录", key='login'), sg.Button("退出", key='exit') ]
]

layout_msg = [
    [sg.Multiline(key='msg_display')],
    [sg.InputText(key='msg_send')],
    [sg.Button("send", key='send')]
]

layout = [
    [sg.Frame('登录',key='win_login',layout=layout_login,visible=True),
     sg.Frame('聊天',key='win_msg',layout=layout_msg,visible=True)]
]

window = sg.Window(jid,layout)
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
        window.Element('win_msg').Update(visible=True)

    if event == 'send':
        msg = values['msg_send']
        print(msg)
        im_send(msg)
        window.Element('msg_send').Update(value='')
        r = window.Element('msg_display')
        r.Update(value=msg+'\n',append=True)

