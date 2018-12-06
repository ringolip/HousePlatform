#-*- coding:utf-8 -*-
from werkzeug.routing import BaseConverter


"""自定义路由转换器"""

class StaticConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(StaticConverter, self).__init__(url_map) # 继承父类的初始化方法
        self.regex = regex # regex是最重要的、不能修改名字、他是自定义正则的关键
