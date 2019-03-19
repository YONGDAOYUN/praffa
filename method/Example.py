# 示例类，类名与文件名必须相同；主返回方法名必须是handler
class Example():
    def __init__(self, event, context, data):
        # 初始化提交过来的参数
        self.event = event
        self.context = context
        self.data = data

    # 这里放业务操作方法

    # 输出给网关的JSON，这里给的是样例代码，根据自己业务情况更换content内容
    def handler(self):

        # 这里调用完业务操作方法后得到content内容
        content = {"code":"0000","data":self.data,"event":self.event}
        return content
