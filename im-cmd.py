# -*- coding: utf-8 -*-

import sys
import logging


import sleekxmpp

gClient = None

def tstart(event):
    print("session started.")
    gClient.send_presence()
    gClient.get_roster()

def tmessage( msg):
    print("recieving message,type:"+msg['type'])
    print(msg)
    if msg['type'] in ('chat', 'normal'):
        #print("recieved:"+msg)
        msg.reply("Thanks for sending\n%(body)s" % msg).send()

def tim(jid,password):
    im = sleekxmpp.ClientXMPP(jid,password)
    im.add_event_handler("session_start", tstart)
    im.add_event_handler("message", tmessage)
    return im

def do_chat():
    jid = "xj0k@chatserver.space"
    password = "1234!@#$"
    server =  ("chatserver.space",5222)

    #global gClient
    gClient = tim(jid,password)

    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.process(block=True)
        print("Done.")
    else:
        print("Unable to connect.")

do_chat()

