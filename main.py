import PySimpleGUIQt as sg

def test1():
    layout = [[sg.Text(' 输入文字.')],
                     [sg.InputText()],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window 标题', layout)

    event, values = window.Read()
    window.Close()

    text_input = values[0]
    print(text_input)

def test2():
    layout = [[sg.Text('请输入用户名和密码',text_color='blue', background_color='green')],
              [sg.Image(filename="/Users/netbox-wangdong/Downloads/logo-srap.png")],
              [sg.Input(default_text="请输入账号",background_color='yellow',text_color='blue')],
              [sg.Input(default_text="请输入密码",password_char='*')],
              [sg.Button('登录',size=(5,2),button_color=('red','yellow'),visible=True,tooltip="click me" ), sg.Button("退出",size=(5,1))]]

    window = sg.Window('pyRoboartIM登录窗口', layout,location=(500,100))


    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        print(event, values)

    window.Close()

test2()
