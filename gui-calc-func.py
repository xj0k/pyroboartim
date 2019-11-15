import sys
import PySimpleGUIQt as sg

buttonSize = (4, 1)
buttonColor = ('white', 'grey')

layout = [
    [sg.InputText(size=(21.5, 1), background_color='white', text_color='black', key='display', disabled=True)],
    [
        sg.Button("1", size=buttonSize, button_color=buttonColor),
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

window = sg.Window('计算器', layout)

def event_equal(calcuInput,disp):
    result = eval(calcuInput)
    print(result)
    disp.update(result)
    return ""

calcuInput = ""
while True:
    event, values = window.read()
    if event in (None, 'exit'):
        window.close()
        break

    disp = window.Element('display')
    if event == '=':
        calcuInput = event_equal(calcuInput,disp)
    elif event == 'c':
        calcuInput = ""
        disp.update(calcuInput)
    else:
        calcuInput += str(event)
        disp.update(calcuInput)
        print(calcuInput)
