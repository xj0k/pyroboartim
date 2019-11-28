# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
import sleekxmpp
import time

gui_debug = True

window = None

jid = "xj0k2@chatserver.space"
password = "1234!@#$"
server = ("chatserver.space", 5222)
gClient = sleekxmpp.ClientXMPP(jid, password)

#mto = "xj0k@chatserver.space"
mto = 'xj0k1234@trillian.im'

txt_wid = 16
size_i = (txt_wid,1)
size_f = (txt_wid,26)
size_b = (6,1)

def update_recv_text(msg):
    txt = window.Element('text')
    m =  "接收:"+msg
    tc = 'blue'
    v = '\n'+ m
    txt.Update(value=v,append=True,text_color=tc)

def update_send_text(msg):
    txt = window.Element('text')
    #m = 'send>' + msg
    m =  "发送："+ msg
    tc = 'blue'
    v = '\n'+ m
    txt.Update(value=v,append=True,text_color=tc)

def send_msg(msg):
    if gui_debug:
        return
    gClient.send_message(mto,msg)

def recv_message(msg):
    t = msg['body']
    update_recv_text(t)

def im_logout():
    if gui_debug:
        return
    gClient.disconnect(wait=True)

def im_login():
    if gui_debug:
        return
    gClient.add_event_handler("message", recv_message)
    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.send_presence()
        gClient.process(block=False)
        print("Done.")
    else:
        print("Unable to connect.")


frm_login = [
    [sg.Image(filename="/users/netbox-wangdong/downloads/logo-srap.png")],
    [sg.Text("Please login")],
    [sg.InputText(key='id', default_text='user id',size=size_i)],
    [sg.InputText(key='password',size=size_i)],
    [sg.Button("login", key='start',size=size_b), sg.Button('exit', key='exit',size=size_b)]
]

frd = ['1xxxx','2xxxx','3xxxx']
frm_friends = [
    [sg.Listbox(values=frd,size=(txt_wid,14))]
]

frm_text = [
    [sg.Multiline(key='text',size=(txt_wid,14),disabled=True)],
    [sg.InputText("",key='message',size=size_i) ],
    [sg.Button('send', key='send',size=size_b), sg.Button('back', key='back',size=size_b)]
]

layout = [
    [sg.Frame('登录',key='frm_login',layout=frm_login,size=size_f),
        sg.Frame('friends',key='frm_friends',layout=frm_friends,visible=True,size=size_f),
        sg.Frame('消息',key='frm_text',layout=frm_text,visible=True,size=size_f)]
]

window = sg.Window("roboartIM",layout)
while True:
    event,values = window.read()
    print(event,values)
    if event == 'exit' or event is None:
        im_logout()
        window.close()
        sys.exit(0)

    if event == 'start':
        print("will start chat process.")
        im_login()
        window.Element('frm_login').Update(visible=False)
        window.Element('frm_text').Update(value=mto,visible=True)

    if event == 'send':
        msg = window.Element('message').Get()
        print("sending message:%s" % msg )
        send_msg(msg)
        window.Element('message').Update(value='')
        update_send_text(str(msg))

    if event == 'recv_test':
        msg = window.Element('recv').Get()
        window.Element('recv').Update(value='')
        update_recv_text(str(msg))

    if event == 'back':
        window.Element('frm_login').Update(visible=True)
        window.Element('frm_text').Update(visible=False)



