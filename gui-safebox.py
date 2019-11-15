import sys,os
import PySimpleGUIQt as sg
import time

buttonSize=(4,1)
buttonColor=('white','grey')
butFont = (1,24)

layout = [
    [sg.InputText(size=(21.5,2),key='display',password_char='*',font=butFont,disabled=True,default_text='')],
    [
        sg.Button("1", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("2", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("3", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("4", size=buttonSize, font=butFont, button_color=buttonColor)
    ],
    [
        sg.Button("5", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("6", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("7", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("8", size=buttonSize,font=butFont, button_color=buttonColor)
    ],
    [
        sg.Button("9", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("0", size=buttonSize,font=butFont, button_color=buttonColor),
        sg.Button("c", size=buttonSize, font=butFont, button_color=buttonColor),
        sg.Button("op", size=buttonSize,font=butFont, button_color=buttonColor)
    ]
]

window = sg.Window('计算器', layout)

inputStr = ""
password = '1234'

def open_win2():
    window.Hide()
    layout2 = [
        [sg.T("Your safe is opened.")],
        [sg.OK()]
    ]
    win2 = sg.Window("windows 2",layout2)
    win2.read()

while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break

    disp = window.Element('display')
    if event == 'op':
        if inputStr==password:
            print("open")
            disp.update(value="opened!")
            sg.popup("opened!")
            open_win2()
        else:
            print("wrong")
            sg.popup("wrong password")
    elif event == 'c':
        inputStr = ''
        disp.update(inputStr)
    else:
        inputStr += str(event)
        disp.update(inputStr)
        print(inputStr)

