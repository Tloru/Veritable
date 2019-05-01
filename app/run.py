from . import *

import flask
from flask import Flask

def run(args):
    """
    the run function makes a flask app and runs it.
    run: takes a list of arguments from the command line
    returns: None
    """
    # setting up
    assert len(args) == 0
    env = auto_env()
    app = Flask(__name__)

    # home page, index
    @app.route('/index')
    @app.route('/')
    def root(): return route("")

    # everything else
    @app.route('/<path:page>')
    def route(page):
        meta([]) # build style for each request
        return parse(page.split("/"), env)

    # static files
    @app.route('/src/<path:path>')
    def src(path):
        nonlocal env
        path = path.split("/")
        full_path = fuzz_path(env.project_path, "src")
        return flask.send_file(full_path)

    app.run(debug=True)
