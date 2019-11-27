import sys,os
import PySimpleGUIQt as sg
import time
import random

buttonSize = (8, 2)
buttonColor = ('white', 'grey')
buttonColorHit = ('white', 'red')
buttonFont = (1, 24)

layout = [
    [sg.InputText(size=(24,2),key='display',font=buttonFont,disabled=True,default_text='请抽奖',justification='center')],
    [
        sg.Button("电脑", key='1',size=buttonSize,font=buttonFont, button_color=buttonColor),
        sg.Button("游戏机", key='2', size=buttonSize,font=buttonFont, button_color=buttonColor),
        sg.Button("假期", key='3',size=buttonSize,font=buttonFont, button_color=buttonColor)
    ],
    [
        sg.Button("手机", key='8', size=buttonSize,font=buttonFont, button_color=buttonColor),
        sg.Button("start",key='start', size=buttonSize,font=buttonFont, button_color=('red','white')),
        sg.Button("电视", key='4', size=buttonSize,font=buttonFont, button_color=buttonColor)
    ],
    [
        sg.Button("冰箱", key='7', size=buttonSize,font=buttonFont, button_color=buttonColor),
        sg.Button("洗衣机", key='6', size=buttonSize,font=buttonFont, button_color=buttonColor),
        sg.Button("汽车", key='5', size=buttonSize,font=buttonFont, button_color=buttonColor)
    ]
]

window = sg.Window('幸运大抽奖', layout)

def choujiang():
    end = random.randint(1, 9)
    for i in range(1, end):
        b = window.Element(str(i))
        b.update(button_color=buttonColorHit)
        window.Refresh()
        time.sleep(0.1)
        b.update(button_color=buttonColor)
        window.Refresh()
        time.sleep(0.1)

    result = "恭喜中奖：" + str(b.GetText())
    disp.update(result)

while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break

    disp = window.Element('display')

    if event == 'start':
       choujiang()
