import os

from mistune import markdown as md
from structured_markdown import inline_style as smd
from m2r import convert as rst

import re

import flask
from flask import Flask

# TODO: HEY, I'M TAKLING TO YOU!
"""
now that I have your attention...
This code needs to:
- go through all the files and dirs in the root and src
- parse md, rst, etc. files into html
- build templates using the flask app
- run the app.
"""

app = Flask("__name__")

counter = 0

class Function:

    def __init__(self, function, name):
        self.function = function
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

class Run:
    def __init__(self, project_path, veritable_path):
        self.project_path = project_path
        self.veritable_path = veritable_path
        self.root_path = os.path.join(self.project_path, "root")
        self.src_path = os.path.join(self.project_path, "src")
        self.routes = {}

        self.markup = {
            "md": md,
            "smd": smd,
            "rst": rst
        }

        self.root_routes()

        self.routes["Home/hello.md"]()

    def root_routes(self):
        for root, dirs, files in os.walk(self.root_path):
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']

            for file in files:
                file_path = os.path.join(root, file)
                path = os.path.relpath(file_path, start=self.root_path)

                extension = file.split(".")[1]

                with open(file_path, "r") as fin:
                    data = fin.read()

                try:
                    parsed = flask.Markup(self.markup[extension](data))
                except KeyError:
                    raise NotImplementedError("Could not parse file type '.{}'".format(extension))

                def x():
                    nonlocal parsed
                    flask.render_template("file.html", file=parsed)

                z = Function(x, name=re.sub("[^0-9a-zA-Z]+", "", path))

                app.route("/" + path)(z)

                self.routes[path] = z

if __name__ == "__main__":
    runner = Run(os.path.abspath("help"), os.path.abspath("veritable"))
