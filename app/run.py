from . import *

import os

import flask
from flask import Flask

def run(args):
    # checking args
    assert len(args) == 0

    # setting up env
    env = auto_env()

    #starting the flask app
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
        path = path.split("/")
        folders, end = path[:-1], path[-1]

        base_path = fuzz_path(join(env.project_path, "src"), folders, env.vignore)
        full_path = fuzz_files(base_path, end, env.vignore)

        return flask.send_file(full_path)

    app.run(debug=True)
