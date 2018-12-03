# -*- coding:utf-8 -*-
"""项目包"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

from config import config
import redis


db = SQLAlchemy()

redis_store = None


# 工厂模式
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name)) # 使用配置

    db.init_app(app) # 延迟初始化
    Session(app) # flask_session
    CSRFProtect(app) # CSRF防护

    # 缓存的存储
    global redis_store
    redis_store = redis.StrictRedis(host=app.config.get("REDIS_HOST"), port=app.config.get("REDIS_PORT"))

    # 注册蓝图
    from api_1_0 import api # 推迟导包
    app.register_blueprint(api, url_prefix="/api/v1.0")

    return app



