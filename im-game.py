# -*- coding: utf-8 -*-

import sys
import turtle
import time
import sleekxmpp
import os

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
jid = 'xj0k1234@trillian.im'
password = '1234!@#$'
server = ("impp.trillian.im", 3158)
gClient = sleekxmpp.ClientXMPP(jid, password)

debug = False

def init_player():
    player = turtle.Turtle()
    player.color("blue")
    player.shape("turtle")
    player.penup()
    #player.speed(0)
    return player

def send_msg(msg):
    #mto = "xj0k@chatserver.space"
    #mto = 'xj0k1234@trillian.im'
    mto = "dengweiyi@chatserver.space"
    mto = "tangjunbin@trillian.im"
    gClient.send_message(mto,msg)


def im_logout():
    send_msg("Robot out, bye!")
    gClient.disconnect(wait=True)

def im_login():
    gClient.add_event_handler("message", recv_msg)
    print('connecting to :%s'%(jid))
    if gClient.connect(server):
        print("Connected, start processing messages.")
        gClient.send_presence()
        gClient.process(block=False)
        print("Done.")
    else:
        print("Unable to connect.")



wn = turtle.Screen()
wn.tracer(2)

step = 5
t1 = init_player()
t2 = init_player()

def mv_left():
    print('move left')
    if not debug:
        send_msg('left')
    t1.goto(t1.xcor() - step, t1.ycor())

def mv_right():
    print('move right')
    if not debug:
        send_msg('right')
    t1.goto(t1.xcor() + step, t1.ycor())

def mv_left2():
    t2.goto(t2.xcor() - step, t2.ycor())

def mv_right2():
    t2.goto(t2.xcor() + step, t2.ycor())

def recv_msg( msg):
    t = msg['body']
    print("receive:%s" % t)

    # mirror action
    if t == 'left':
        mv_right2()
    elif t =='right':
        mv_left2()
    else:
        print("unknow command received")


# boarder of the space
miny=-300
maxx=300
maxy=300
minx=-300

pen = turtle.Turtle()
def draw_border():
    pen.color("white")
    pen.penup()
    pen.setposition(minx,miny)
    pen.pendown()
    pen.pensize(3)
    for side in range(4):
        pen.forward(maxx-minx)
        pen.left(90)
    pen.hideturtle()

turtle.listen()
turtle.onkey(mv_left,"Left")
turtle.onkey(mv_right,"Right")

t1.hideturtle()
t1.goto(0,miny+20)
t1.showturtle()

t2.hideturtle()
t2.goto(0,maxy-20)
t2.color('red')
t2.showturtle()

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.goto(minx+100,0)
pen2.write("loading")

if not debug:
    im_login()
pen2.write(" done!")
time.sleep(2)
pen2.clear()
pen2.up()
pen2.goto(minx+10,miny+10)
pen2.hideturtle()

while True:
    pen2.left(3)
    time.sleep(0.01)

