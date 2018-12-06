#-*- coding:utf-8 -*-
from flask import Blueprint, current_app, make_response
from flask_wtf import csrf

"""返回静态资源的蓝图"""


resource = Blueprint("static_resource", __name__)

@resource.route('/<re(".*"):static_resource>')
def get_resource(static_resource):
    if static_resource == "": # url为则返回主页
        static_resource = "index.html"

    if static_resource != "favicon.ico": # 如果访问的不是favicon
        static_resource = "html/" + static_resource # 资源存储在static/html文件夹

    resp = make_response(current_app.send_static_file(static_resource)) # send_static_file()返回静态文件
    
    # 生成CSRF token
    csrf_token = csrf.generate_csrf()
    resp.set_cookie("scrf_token", csrf_token) # 将token设置在cookie里
    
    return resp # 返回携带csrf_token的响应