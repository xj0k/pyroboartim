import sys
import PySimpleGUIQt as sg
'''
'''
layout = [
    [sg.InputText()],
    [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.B('+')],
   [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.B('=')]
]
window = sg.Window('计算器', layout)

str=""
while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break
    if event == '=':
        print(eval(str))
        str = ""
    str = str+event
    print(str)

