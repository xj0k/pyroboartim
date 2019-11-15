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

'''
event, values = window.Read()
window.Close()

text_input = values[0]
print(text_input)
'''

while True:
    event, values = window.read()
    print(event, values)
    if event == 'exit' or event is None:
        window.close()
        sys.exit(0)
    else:
        print("user:"+values[1]+" pass:"+values[2])
        sg.Popup("will go on to chat.")
