# 示例类，类名与文件名必须相同；主返回方法名必须是handler
class example():
    def __init__(self):
        pass

    def handler(self, data):
        content = {"code":"0000","data":data}
        return content