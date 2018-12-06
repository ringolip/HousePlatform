# -*- coding:utf-8 -*-
from flask import Blueprint

"""视图函数蓝图"""

api = Blueprint("api_1_0", __name__)

from .demo import index
from .image_code import image_code