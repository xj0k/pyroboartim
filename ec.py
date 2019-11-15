# -*- coding: utf-8 -*-

import sys
import logging
import getpass
from optparse import OptionParser


import PySimpleGUI as sg
import sleekxmpp

if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')
else:
    raw_input = input

class EchoBot(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    def start(self, event):
        print("session started.")
        self.send_presence()
        self.get_roster()
        #self.disconnect(wait=True)

    def message(self, msg):
        print("recieving message,type:"+msg['type'])
        print(msg)
        if msg['type'] in ('chat', 'normal'):
            #print("recieved:"+msg)
            msg.reply("Thanks for sending\n%(body)s" % msg).send()
            if msg['body'] == "END":
                print("end session")
                self.disconnect()


#gClient = sleekxmpp.ClientXMPP("","")
gClient = None

def tstart(event):
    print("session started.")
    gClient.send_presence()
    gClient.get_roster()
    #self.disconnect(wait=True)

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

def do_chat(noneOO):
    jid = "xj0k2@chatserver.space"
    password = "1234!@#$"
    server =  ("chatserver.space",5222)

    if noneOO:
        print("-- None OO mode --")
        global gClient
        im = tim(jid,password)
        gClient = im
    else:
        im = EchoBot(jid, password)

    im.register_plugin('xep_0030') # Service Discovery
    im.register_plugin('xep_0004') # Data Forms
    im.register_plugin('xep_0060') # PubSub
    im.register_plugin('xep_0199') # XMPP Ping


    # Connect to the XMPP server and start processing XMPP stanzas.
    if im.connect(server):
        print("Connected, start processing messages.")
        im.process(block=True)
        print("Done.")
    else:
        print("Unable to connect.")

def window_test(noneOO):
    layout = [
        [sg.Text("Will start chat.")],
        [sg.OK('start'),sg.Cancel('exit')]
    ]
    window = sg.Window("开始聊天",layout)
    while True:
        event,values = window.read()
        print(event,values)
        if event == 'exit' or event is None:
            window.close()
            sys.exit(0)
        else:
            sg.Popup("will go on to chat.")
            do_chat(noneOO)


if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)
    optp.add_option('-n', '--noneOO', help='set mode to non-OO',
                    action='store_const', dest='mode',
                    const=True, default=False)
    optp.add_option('-w', '--window', help='start with widow.',
                    action='store_const', dest='window',
                    const=True, default=False)

    opts, args = optp.parse_args()

    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    if opts.window:
        window_test(opts.mode)
    else:
        do_chat(opts.mode)

