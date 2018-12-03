# -*- coding:utf-8 -*-
import redis

"""配置文件"""

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



class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置"""
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

 

