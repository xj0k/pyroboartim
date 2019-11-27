import time
import os
import urllib.request
import json
#import urllib3


# Turing API
TURING_KEY = "a7a5b730121a4da5b2d190edb668862b"
API_URL = "http://openapi.tuling123.com/openapi/api/v2"


# 图灵处理
def robot_resp(text_input):
    req = {
        "perception":
            {
                "inputText":
                    {
                        "text": text_input
                    },

                "selfInfo":
                    {
                        "location":
                            {
                                "city": "珠海",
                                "province": "广东",
                                "street": "唐人街"
                            }
                    }
            },
        "userInfo":
            {
                "apiKey": TURING_KEY,
                "userId": "roboart"
            }
    }
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(API_URL, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    return results_text

if __name__ == '__main__':
   #robot_resp("今天天气怎么样？")
   print(robot_resp("讲个故事`"))
