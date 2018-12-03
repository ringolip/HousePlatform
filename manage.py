# -*- ccoding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import redis

class Config(object):
    """配置信息"""
    # 秘钥配置用于CSRF和session
    SECRET_KEY = "ringo"

    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/houses'
    # 在数据库改动的时候会自动修改模型类相关的信息
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    # session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True # 对发送给cookie的session进行加密
    PERMANENT_SESSION_LIFETIME = 86400 # session的过期时间


app = Flask(__name__)
app.config.from_object(Config) # 使用配置类

db = SQLAlchemy(app)
Session(app) # flask_session
CSRFProtect(app) # CSRF防护


#缓存的存储
redis_store = redis.StrictRedis(host=app.config.get("REDIS_HOST"), port=app.config.get("REDIS_PORT"))


@app.route('/')
def index():
    return "index page"


if __name__ == "__main__":
    app.run()