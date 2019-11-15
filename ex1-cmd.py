# -*- coding: utf-8 -*-

import time
import sleekxmpp

jid = "tangjunbin@chatserver.space"
password = "tangjunbin"
fr = "xj0k@chatserver.space"

server = ("chatserver.space", 5222)

# 初始化客户端程序
client = sleekxmpp.ClientXMPP(jid, password)

# 连接服务器
state = client.connect(server)
if state is False:
    print("connect failed.")
    exit(1)

print("链接服务器成功,开始处理消息")
client.process(block=False)

client.send_presence()
print("发送在线状态通知")

client.send_message(fr,"收到我的消息了吗")
# 需要等待几秒钟让消息发送处理完成
time.sleep(5)
print("发送消息完成")

client.disconnect(wait=True)
print("断开连接")

print("程序结束")

