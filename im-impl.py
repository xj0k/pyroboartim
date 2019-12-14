# -*- coding: utf-8 -*-

import sys
import PySimpleGUI as sg
import sleekxmpp
import time

gui_debug = False

window = None
#sg.ChangeLookAndFeel('SandyBeach')
bgcolor = 'lightslategrey'
bgcolor = 'beige'
bgcolor = 'silver'
bgcolor = 'whitesmoke'

jid = "xj0k2@chatserver.space"
password = "1234!@#$"
server = ("chatserver.space", 5222)

jid = 'test1@localhost'
password = '123456'
server = ("192.168.3.218", 5222)

gClient = sleekxmpp.ClientXMPP(jid, password)

#mto = "xj0k@chatserver.space"
mto = 'xj0k1234@trillian.im'
mto = 'test2@localhost'

txt_wid = 16
size_i = (txt_wid,1)
size_f = (txt_wid,26)
size_b = (6,1)

friends = []

def update_recv_text(f,msg):
    txt = window.Element('text')
    m =  "接收<-(" + f + ')' +msg
    tc = 'blue'
    v = '\n'+ m
    txt.Update(value=v,append=True,text_color=tc)

def update_send_text(to,msg):
    v = '\n' + '发送->('+ str(to) +')'+ msg
    tc = 'blue'
    window.Element('text').Update(value=v,append=True,text_color=tc)

def send_msg(to,msg):
    if gui_debug:
        return
    gClient.send_message(to,msg)

def recv_message(msg):
    f = msg['from'].bare
    t = msg['body']
    print("recv:%s" % t)
    update_recv_text(f,t)

def session_start(event):
    global friends
    print("session started.")
    gClient.send_presence()
    print("presence sent, getting rosters.")
    iq = gClient.get_roster()
    print("roster info")
    for j, i in iq['roster']['items'].items():
        print("Adding roster:jid:%s" % j)
        friends.append(str(j))

def im_logout():
    if gui_debug:
        return
    gClient.disconnect(wait=True)

def im_login():
    if gui_debug:
        return
    gClient.add_event_handler("session_start", session_start)
    gClient.add_event_handler("message", recv_message)
    if gClient.connect(server):
        print("Connected, start processing messages.")
        #gClient.send_presence()
        gClient.process(block=False)
        print("Done.")
    else:
        print("Unable to connect.")

def make_layout():
    frm_login = [
        [sg.Image(filename="logo-srap.png")],
        [sg.Text("Please login")],
        [sg.InputText(key='id', default_text=jid,size=size_i)],
        [sg.InputText(key='password',size=size_i)],
        [sg.Button("login", key='start',size=size_b), sg.Button('exit', key='exit',size=size_b)]
    ]

    frd = ['1xxxx','2xxxx','3xxxx']
    col_frd = [
        [ sg.Listbox(values=frd,size=(txt_wid,16),key='friends',background_color=bgcolor,no_scrollbar=True) ],
        [sg.Button('刷新', key='refresh',size=size_b)]
        ]

    col_text = [
        [sg.Multiline(key='text',size=(txt_wid*2,14),disabled=True,border_width=0,autoscroll=True)],
        [sg.InputText("",key='message',size=size_i) ],
        [sg.Button('send', key='send',size=size_b,bind_return_key=True,visible=False), sg.Button('back', key='back',size=size_b)]
    ]
    frm_text = [
        [sg.Column(col_frd,background_color=bgcolor),
           sg.Column(col_text,background_color=bgcolor)]
    ]

    layout = [
        [sg.Frame('登录',key='frm_login',layout=frm_login,size=size_f,background_color=bgcolor),
        sg.Frame('消息',key='frm_text',layout=frm_text,visible=True,size=size_f,background_color=bgcolor)]
    ]
    return layout

def gui_login(values):
    print("will start chat process.")
    im_login()
    window.Element('frm_login').Update(visible=False)
    window.Element('frm_text').Update(value="",visible=True)
    window.Element('friends').Update(values=friends)

def gui_sendmsg(values):
    #msg = window.Element('message').Get()
    msg = values['message']
    s = values['friends']
    if s:
        to = s[0]
    else:
        to = mto
    print("sending message:%s->:%s" % (to,msg) )
    send_msg(to,msg)
    update_send_text(to,str(msg))
    window.Element('message').Update(value='')

window = sg.Window("roboartIM",make_layout(),return_keyboard_events=False)
while True:
    event,values = window.read()
    print(event,values)
    if event == 'exit' or event is None:
        im_logout()
        window.close()
        sys.exit(0)

    if event == 'start':
        gui_login(values)

    if event == 'refresh':
        window.Element('friends').Update(values=friends)

    if event == 'send':
        gui_sendmsg(values)

    if event == 'back':
        window.Element('frm_login').Update(visible=True)
        window.Element('frm_text').Update(visible=False)

    if event == 'recv_test':
        msg = window.Element('recv').Get()
        window.Element('recv').Update(value='')
        update_recv_text(str(msg))
