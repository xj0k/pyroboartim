# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
import sleekxmpp

window = None

jid = "xj0k2@chatserver.space"
password = "1234!@#$"
server = ("chatserver.space", 5222)
gClient = sleekxmpp.ClientXMPP(jid, password)


def send_msg(msg):
    mto = "xj0k@chatserver.space"
    gClient.send_message(mto,msg)

def im_logout():
    gClient.disconnect(wait=True)

def im_login():
    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.send_presence()
        gClient.process(block=False)
        print("Done.")

layout = [
    [sg.Text("Will start chat.")],
    [sg.InputText(key='message',default_text='please input message here')],
    [sg.Button("login",key='start')],
    [sg.Button('send',key='send'),sg.Button('exit',key='exit')]
]
window = sg.Window("chatting",layout)
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


