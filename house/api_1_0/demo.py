from . import api
import logging
from flask import current_app

@api.route('/')
def index():
    current_app.logger.info("iiiiiii")
    current_app.logger.debug("dddddd")
    current_app.logger.error("reeeeee")
    current_app.logger.warn("wwwwwww")
    return "index page for v1.0"