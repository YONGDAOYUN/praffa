# -*- coding: utf-8 -*-
# 引入包
import json
import base64
from method import *

# 主启动函数
def handler(event, context):
    event = json.loads(event)
    # 接收到网关传递函数关键变量
    queryMethod = event['queryParameters']['method']
    data = (base64.b64decode(event['body'].encode('utf-8'))).decode()
    data = json.loads(data)
    # 根据不同的METHOD调用不同类库完成业务
    class_dir = queryMethod + '.'
    class_name = eval(class_dir + queryMethod)
    # 实例化对应的类
    MethodClass = class_name(event, context, data)
    # 完成业务，返回数据
    content = MethodClass.handler()
    # 组织业务数据，body里的data原封不动的交给类去处理
    rep = {
        "isBase64Encoded": "False",
        "statusCode": "200",
        "headers": {
            "x-custom-header": "no"
        },
        "body": content
    }
    # 向API网关返回数据
    return json.dumps(rep)
