# -*- coding: utf-8 -*-

# 导入系统库
import sys
# 导入图形界面（GUI）库
import PySimpleGUI as sg
# 导入网络（XMPP）处理库
import sleekxmpp


# 用户名和密码
jid = "fengyijun@chatserver.space"
password = 'fengyijun'
# 服务器地址
server = ("chatserver.space", 5222)
# 创建一个聊天协议XMPP的辅助客户端对象，用于后续的网络数据处理
gClient = sleekxmpp.ClientXMPP(jid, password)

#  ---------------  下面的代码主要实现与网络相关的功能  -----------------
# 消息发送的函数
def im_send(msg):
    # 接收消息的朋友账号
    mto = 'xj0k1234@trillian.im'
    mto = 'dengweiyi@chatserver.space'
    print("开始发送:%s" % msg)
    # 通过网络先朋友发送信息
    gClient.send_message(mto,msg)

    # 在每一个发送的消息后增加一个换行符号（\n），后续的聊天内容就会出现在下一行
    m = msg + '\n'
    # 将发送的内容展现在名为'msg_display'的文本框中（一个多行的文本框，MultilineInput）
    r = window.Element('msg_display').Update(value=m,append=True)

# 接收消息的处理函数,本函数通过gClient.add_event_handler注册到网络消息的事件处理过程中
# 放xmpp的客户端（gClient）接收到消息时会自动执行本函数
# 本函数实现接收内容再文本框中的展现，处理过程与im_send基本一致。
def recv_msg(msg):
    m = msg['body']
    print("接收到消息，内容:%s" % m)
    m = m + '\n'
    r = window.Element('msg_display')
    r.Update(value=m,append=True)

# 实现网络（xmpp）登录过程的函数
def im_login():
    # 首先注册消息处理函数
    gClient.add_event_handler('message',recv_msg)

    print("开始登录，用户名:%s" % jid)
    # 链接服务器
    if gClient.connect(server):
        print("链接成功，开始发送在线状态")
        # 发送在线状态,这样好友才能够看到自己已经处于在线状态，可以开始聊天
        gClient.send_presence()
        # 启动消息处理过程，必须包含这个代码，消息才可以发送和接收。
        gClient.process(block=False)
        print("开始处理消息.")

# 退出网络的函数
def im_logout():
    # 直接断开链接即可。
    gClient.disconnect(wait=True)

# ----------------- 下面的代码处理图形界面（GUI）展现和用户操作 ---------------

# 登录窗口布局
layout_loginin = [
    [sg.Text("请登录")],
    [sg.Button("登录", key='login'), sg.Button('退出', key='exit')]
]
# 聊天窗口布局
layout_chat = [
    [sg.Multiline(key='msg_display')],
    [sg.InputText(key='msg_send'), sg.Button("发送", key='send')],
]

# 图形界主窗体布局，包含'登录窗口'和'聊天窗口'
layout = [
    # 初始状态下，登录窗口处于看见状态（visible=True）,聊天窗口处于不可见状态（visible=False）
   [ sg.Frame('登录窗口',key='win_login',layout=layout_loginin,visible=True),
     sg.Frame('聊天窗口',key='win_chat',layout=layout_chat,visible=False)]
]

# 利用上面设计的布局，创建图形界面主窗体，并展现出来
window = sg.Window(jid,layout)

# 下面的代码基于图形界面事件机制，完成用户操作的功能
while True:
    # 读取窗口事件和各个GUI元素的值
    event,values = window.read()
    print(event,values)

    # 关闭和'退出'按钮点击的事件
    if event == 'exit' or event is None:
        print('退出程序')
        # 退出网络客户端
        im_logout()
        # 关闭窗口
        window.close()
        # 程序退出
        sys.exit(0)

    # '登录'按钮点击事件的处理
    if event == 'login':
        print("开始登录.")
        # 执行上面实现的网络登录
        im_login()
        # 登录成功后，设置登录窗口不可见，设置聊天窗口可见
        window.Element('win_login').Update(visible=False)
        window.Element('win_chat').Update(visible=True)

    # '发送'按钮点击的事件处理
    if event == 'send':
        imsg = values['msg_send']
        print(imsg)
        # 执行网络发送聊天内容的函数
        im_send(imsg)

