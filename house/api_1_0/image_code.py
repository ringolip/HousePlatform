#-*- coding:utf-8 -*-

"""图片验证码视图"""
from . import api
from flask import current_app, make_response, jsonify
from house.utils.captcha.captcha import captcha
from house import redis_store
from house.utils.constants import IMAGE_CODE_REDIS_EXPIRES
from house.utils.response_code import RET


@api.route('/imagecode/<image_code>')
def image_code(image_code):
    # 1. 获取参数
    # 2. 检验参数
    # 3. 业务逻辑处理
        # 生成验证码图片
        # 将验证码编号 和 验证码真实值保存在redis
        # 返回图片

    name, text, image = captcha.generate_captcha() # 返回验证码名字、真实值、图片二进制编码

    # 测试异常
    try:
        redis_store.setex(image_code, IMAGE_CODE_REDIS_EXPIRES, text) # 将验证码编号、真实值存入redis字符串格式
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="save failed") #返回json

    resp = make_response(image)
    resp.headers["Content-Type"] = "image/jpg"

    # 4. 返回值
    return resp


    