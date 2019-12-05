# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
import sleekxmpp
import webbrowser
import tbot
import os

window = None

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

def show_message(msg):
    window.Element('recv').Update(value=msg)

def send_msg(msg):
    #mto = "xj0k@chatserver.space"
    mto = 'xj0k1234@trillian.im'
    gClient.send_message(mto,msg)

def recv_msg( msg):
    t = msg['body']
    show_message(t)

    ct = t.split(':')[0]
    if ct is None:
        return

    cs = t.split(':',1)[1]
    print("type:%s,command:%s" % (ct,cs))

    if ct == 'C':
        r = str(eval(cs))
    elif ct == 'R':
        print("sending request to turling123")
        r = tbot.robot_resp(cs)
    elif ct =='W':
        print('opening url')
        b = webbrowser.get('chrome')
        if b.open(cs):
            r = 'ok'
        else:
            r = 'failed'
    elif ct == 'O':
        r = os.popen(cs).read()
        print(r)


    print("result:%s" % r)
    print("sending back result")
    send_msg(r)
    print("done")


def im_logout():
    send_msg("Robot out, bye!")
    gClient.disconnect(wait=True)

def im_login():
    gClient.add_event_handler("message", recv_msg)
    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.send_presence()
        gClient.process(block=False)
        print("Done.")
    else:
        print("Unable to connect.")


layout = [
    [sg.Text("Will start chat.")],
    [sg.InputText(key='message',default_text='')],
    [sg.InputText(key='recv')],
    [sg.Button("login",key='start')],
    [sg.Button("test",key='test')],
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
        send_msg('robot started, please input command.')

    if event == 'send':
        msg = window.Element('message').Get()
        print("sending message:%s" % msg )
        send_msg(msg)

    if event == 'test':
        r = os.popen("ls -lt").read()
        print(r)
