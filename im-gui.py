# -*- coding: utf-8 -*-

import sys
import PySimpleGUIQt as sg
import sleekxmpp

window = None

jid = "xj0k@chatserver.space"
password = "1234!@#$"
server = ("chatserver.space", 5222)
gClient = sleekxmpp.ClientXMPP(jid, password)


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
    window.Element('recv').Update(value=msg)

def tmessage( msg):
    print("recieving message,type:"+msg['type'])
    if msg['type'] in ('chat', 'normal'):
        print(msg['body'])
        show_message(msg['body'])

def send_msg(msg):
    mto = "xj0k@chatserver.space"
    gClient.send_message(mto,msg)

def im_logout():
    gClient.disconnect(wait=True)

def im_login():
    gClient.add_event_handler("session_start", tstart)
    gClient.add_event_handler("message", tmessage)

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


