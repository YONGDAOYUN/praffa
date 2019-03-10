# praffa是什么？
Python Restful Api Farmwok For Aliyun的首字母简写。是一款针对阿里云的函数计算+API网关产品开发的轻型框架。
# 开发说明
* 在method里的Example是示例类，类文件名、类名、method**三者同名**，建议采用大驼峰规则定义，例如：GetUserInfo  
* 主返回方法名必须是handler，并且放在类方法的最后一个。其他代码自己是自己业务代码。  
* 类库文件增删改要在__init__.py文件里报备哦。如：`__all__ = ["Example.py"]`  
* method放到API网关配置的Query里，配置为映射方式，body为非表单提交模式的JSON
# 图解从零开始