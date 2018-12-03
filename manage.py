# -*- ccoding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import redis

class Config(object):
    """配置信息"""
    # 秘钥配置用于表单
    SECRET_KEY = "ringo"

    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/houses'
    # 在数据库改动的时候会自动修改模型类相关的信息
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"



app = Flask(__name__)
app.config.from_object(Config) # 使用配置类

db = SQLAlchemy(app)

redis.StrictRedis(host=app.config.get("REDIS_HOST"),port=app.config.get("REDIS_PORT"))


@app.route('/')
def index():
    return "index page"


if __name__ == "__main__":
    app.run()