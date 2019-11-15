import sys,os
import PySimpleGUIQt as sg
import time
import random

'''
    基于计算器修改的抽奖程序：
    1） 利用按钮作为抽奖循环的奖品选择
    2） 想按钮增加'key'属性，方便定位按钮和处理按钮事件
    3） 利用随机（random）实现随机抽奖的计数器
    4） 利用按钮的Update方法更新按钮背景色的变化，制造出抽奖转盘的效果
'''

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

while True:
    event, values = window.read()
    if event in (None,'exit'):
        window.close()
        break

    disp = window.Element('display')

    if event == 'start':
        end = random.randint(1, 9)
        for i in range(1, end):
            '''
                按钮的处理过程：
                将参与抽奖的各个按钮的key设置为顺序的数字，这样方便使用for进行循环选择
                更新按钮颜色为红色
                使用window.Refresh()实现窗口显示的实时刷新，所以可以看到按钮更新的效果
                延迟100毫秒，方便用户看清楚颜色的变化
                将颜色更新为为原来的颜色
            '''
            b = window.Element(str(i))
            b.update(button_color=buttonColorHit)
            window.Refresh()
            time.sleep(0.1)
            b.update(button_color=buttonColor)
            window.Refresh()
            time.sleep(0.1)

        result = "恭喜中奖：" + str(b.GetText())
        disp.update(result)

