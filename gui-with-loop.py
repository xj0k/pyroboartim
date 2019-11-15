import sys
import PySimpleGUIQt as sg

layout = [
    [sg.T('用户名:'),sg.InputText(key='user')],
    [sg.T('密码:'),sg.InputText(key='pass')],
    [sg.Button('登录'), sg.Cancel('exit')]
]
window = sg.Window('登录', layout)
while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break
    print(event)
    print(values['user'])

