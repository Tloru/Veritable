from . import *

import flask
from flask import Flask

def run(args):
    assert len(args) == 0
    env = auto_env()
    app = Flask(__name__)

    @app.route('/index')
    @app.route('/')
    def root(): return route("")

    @app.route('/<path:page>')
    def route(page):
        meta([]) # build style for each request
        nonlocal env
        return parse(page.split("/"), env)

    @app.route('/src/<path:path>')
    def src(path):
        nonlocal env
        path = path.split("/")
        full_path = fuzz_path(env.project_path, "src")
        return flask.send_file(full_path)

    app.run(debug=True)
