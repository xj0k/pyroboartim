# -*- coding: utf-8 -*-

import sys
import PySimpleGUIQt as sg
import sleekxmpp

window = None

jid = "xj0k2@chatserver.space"
password = "1234!@#$"
server = ("chatserver.space", 5222)
gClient = sleekxmpp.ClientXMPP(jid, password)

def update_text(msg):
    txt = window.Element('text')
    t = txt.Get()
    if t:
        v = txt.Get() + '\n' +msg
        print("current message:%s" % t)
    else:
        v = msg
    txt.Update(value=v)


def show_message(msg):
    window.Element('recv').Update(value=msg)

def send_msg(msg):
    return
    mto = "xj0k@chatserver.space"
    mto = 'xj0k1234@trillian.im'
    gClient.send_message(mto,msg)

def recv_message( msg):
    t = msg['body']
    show_message(t)
    #update_text(t)

def im_logout():
    gClient.disconnect(wait=True)

def im_login():
    gClient.add_event_handler("message", recv_message)
    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.send_presence()
        gClient.process(block=False)
        print("Done.")
    else:
        print("Unable to connect.")


col_chat = [
    [sg.Multiline(key='text',size=(16,6))],
    [sg.InputText("message here to send",key='message'), sg.Button('send', key='send')]
]

col_login = [
    [sg.Image(filename="/users/netbox-wangdong/downloads/logo-srap.png")],
    [sg.Text("Please login")],
    [sg.InputText(key='id', default_text='user id')],
    [sg.InputText(key='password')],
    [sg.Button("login", key='start'), sg.Button('exit', key='exit')]
]

layout = [
    [sg.Column(col_login),sg.Column(col_chat)]
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

    if event == 'send':
        msg = window.Element('message').Get()
        print("sending message:%s" % msg )
        send_msg(msg)
        window.Element('message').Update(value='')
        update_text(str(msg))


