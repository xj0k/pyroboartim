# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
import sleekxmpp

gClient = None
window = None

def tstart(event):
    print("session started.")
    gClient.send_presence()
    print("presence sent, getting rosters.")

    iq = gClient.get_roster()
    print("roster info")
    for j, i in iq['roster']['items'].items():
        print("jid:%s" % j)
        print(i['name'])
        print(i['groups'])

def show_message(msg):
    #sg.PopupCancel(msg)
    window.Element('recv').Update(value=msg)

def tmessage( msg):
    print("recieving message,type:"+msg['type'])
    if msg['type'] in ('chat', 'normal'):
        print(msg['body'])
        show_message(msg['body'])

def tim(jid,password):
    im = sleekxmpp.ClientXMPP(jid,password)
    im.add_event_handler("session_start", tstart)
    im.add_event_handler("message", tmessage)
    return im

def send_msg(msg):
    mto = "xj0k@chatserver.space"
    gClient.send_message(mto,msg)

def stop_chat():
    gClient.disconnect(wait=True)

def start_chat():
    jid = "xj0k2@chatserver.space"
    password = "1234!@#$"
    server = ("chatserver.space",5222)

    global gClient
    gClient = tim(jid,password)

    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.process(block=False)
        print("Done.")
    else:
        print("Unable to connect.")



layout = [
    [sg.Text("Will start chat.")],
    [sg.InputText(key='message',default_text='please input message here')],
    [sg.InputText(key='recv')],
    [sg.Button("start chat",key='start')],
    [sg.Button('send',key='send'),sg.Button('exit',key='exit')]
]
window = sg.Window("chatting",layout)
while True:
    event,values = window.read()
    print(event,values)
    if event == 'exit' or event is None:
        stop_chat()
        window.close()
        sys.exit(0)

    if event == 'start':
        print("will start chat process.")
        start_chat()

    if event == 'send':
        msg = window.Element('message').Get()
        print("sending message:%s" % msg )
        send_msg(msg)


