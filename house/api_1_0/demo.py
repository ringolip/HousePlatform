from . import api

@api.route('/')
def index():
    return "index page for v1.0"