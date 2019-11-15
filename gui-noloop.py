import sys
import PySimpleGUIQt as sg

layout = [
    [sg.Image(filename="/Users/netbox-wangdong/Downloads/42-logo.png")],
    [sg.Text(' 请登录')],
    [sg.InputText()],
    [sg.InputText()],
    [sg.Button("ok"), sg.Cancel()]
]

window = sg.Window('登录', layout)

event, values = window.Read()
window.Close()

text_input = values[1]
print(text_input)

