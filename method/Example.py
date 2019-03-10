# 示例类，类名与文件名必须相同；主返回方法名必须是handler
class Example():
    def __init__(self):
        pass

    # 这里放业务操作代码

    def handler(self, data):
        content = {"code":"0000","data":data}
        return content
