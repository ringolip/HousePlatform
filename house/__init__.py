# -*- coding:utf-8 -*-
"""项目包"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

from config import config
import redis
import logging
from logging.handlers import RotatingFileHandler
from .utils.commons import StaticConverter 

db = SQLAlchemy()

redis_store = None

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)



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

    app.url_map.converters["re"] = StaticConverter # 在url_map.converters中传入自定义转换器的映射

    # 注册蓝图
    from api_1_0 import api # 推迟导包
    app.register_blueprint(api, url_prefix="/api/v1.0")

    # 注册静态资源路由
    from .static_resource import resource
    app.register_blueprint(resource)

    return app



