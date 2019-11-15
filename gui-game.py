import sys
import PySimpleGUIQt as sg

'''
layout = [
    [sg.Image(filename="/Users/netbox-wangdong/Downloads/42-logo.png",enable_events=True,key="logo")],
    [sg.T('用户名:'),sg.InputText(key='i_id')],
    [sg.T('密码:'),sg.InputText(key='i_pass')],
    [sg.ProgressBar(max_value=20,bar_color=('red','yellow'), key='pbar')],
    [sg.Button('up',key='up')],
    [sg.Button(button_text='loginfdsafds',key='login',bind_return_key=True), sg.Cancel('exit',key='Exit')]
]
    [sg.Output(size=(4,1),background_color='white',text_color='black')],
'''
buttonSize=(4,1)
buttonColor=('white','grey')

'''
layout = [
    [sg.InputText(size=(21,1),background_color='white',text_color='black',key='display')],
    [
        sg.Button("1", size=buttonSize,button_color=buttonColor),
        sg.Button("2", size=buttonSize, button_color=buttonColor),
        sg.Button("3", size=buttonSize, button_color=buttonColor),
        sg.Button("+", size=buttonSize, button_color=buttonColor),
        sg.Button("-", size=buttonSize, button_color=buttonColor)
    ],
    [
        sg.Button("4", size=buttonSize, button_color=buttonColor),
        sg.Button("5", size=buttonSize, button_color=buttonColor),
        sg.Button("6", size=buttonSize, button_color=buttonColor),
        sg.Button("*", size=buttonSize, button_color=buttonColor),
        sg.Button("/", size=buttonSize, button_color=buttonColor)
    ],
    [
        sg.Button("7", size=buttonSize, button_color=buttonColor),
        sg.Button("8", size=buttonSize, button_color=buttonColor),
        sg.Button("9", size=buttonSize, button_color=buttonColor),
        sg.Button("c", size=buttonSize, button_color=buttonColor),
        sg.Button("=", size=buttonSize, button_color=buttonColor)
    ]
]
'''

layout = [
    [sg.InputText(size=(12,1),key='display')],
    [sg.Button("1"), sg.Button("2"), sg.Button("3" ), sg.Button("+"), sg.Button("-")],
    [sg.Button("4"), sg.Button("5"), sg.Button("6" ), sg.Button("*"), sg.Button("/")],
    [sg.Button("7"), sg.Button("8"), sg.Button("9" ), sg.Button("c"), sg.Button("=")],
    ]
window = sg.Window('计算器', layout)

calcuInput = ""
while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break
    print(event)
    print(values)

    disp = window.Element('display')
    if event == '=':
        result = eval(calcuInput)
        print(result)
        disp.update(result)
        calcuInput = ""
    elif event == 'c':
        calcuInput = ""
        disp.update(calcuInput)
    else:
        calcuInput += str(event)
        print(calcuInput)
        disp.update(calcuInput)

