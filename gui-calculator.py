import sys,os
import PySimpleGUIQt as sg
import time
import random

buttonSize=(8,2)
buttonColor=('white','grey')
butFont = (1,24)

layout = [
    [sg.InputText(size=(21.5,2),key='display',font=butFont,disabled=True,default_text='0')],
    [
        sg.Button("耳机", key='1', size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("优盘", key='2',size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("帅哥", key='3',size=buttonSize,font=butFont, button_color=buttonColor)
    ],
    [
        sg.Button("*", key='4',size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("*", key='5',size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("*", key='6',size=buttonSize,font=butFont, button_color=buttonColor)
    ],
    [
        sg.Button("7", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("8", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("9", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("开始！",key='start', size=buttonSize,font=butFont, button_color=buttonColor)
    ]
]

window = sg.Window('计算器', layout)

calcuStr = ""
while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break

    disp = window.Element('display')

    if event == 'start':
        end = random.randint(1,9)
        for i in range(1, end):
            key = str(i)
            b = window.Element(key)
            b.update(button_color=('white', 'red'))
            window.Refresh()
            time.sleep(0.3)
            b.update(button_color=('white', 'grey'))
            window.Refresh()
            time.sleep(0.3)
        sg.popup("恭喜中奖："+b.GetText())
        continue

        result = eval(calcuStr)
        print(result)
        disp.update(result)
        calcuStr = str(result)
    elif event == 'c':
        calcuStr = ''
        disp.update(calcuStr)
    else:
        calcuStr += str(event)
        disp.update(calcuStr)
        print(calcuStr)

