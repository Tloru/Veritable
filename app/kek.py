from . import *

import os

from fuzzywuzzy import fuzz
import unicodedata

import flask
from flask import Flask

class PageToPath:
    def __init__(self, path_list, addition=""):
        # starting vars
        self.path_list = path_list
        self.addition = addition

        # constants
        self.env = auto_env()
        self.file_fuzz = 0
        self.folder_fuzz = 90
        self.base_path = join(self.env.project_path, addition)

        # get the path
        self.path = self._fuzz_path(self.base_path, path_list)

    def __call__(self):
        return self.path

    def __str__(self):
        return self.path

    def __repr__(self):
        return "Page({!r}, {!r})".format(self.path_list, self.addition)

    def render_page(self):
        pass

    def render_file(self):
        pass

    def render_folder(self):
        pass

    def _filter_folders(self, path):
        folders = [x for x in os.listdir(path) if os.path.isdir(join(path, x))]
        folders = list(filter(self.env.vignore, folders))
        folders = list(filter(lambda x: False if x == "src" else True, folders))
        return folders

    def _filter_files(self, path):
        files = [x for x in os.listdir(path) if os.path.isfile(join(path, x))]
        files = list(filter(self.env.vignore, files))
        return files

    def _simplify(self, string):
        """
        string: a str-like object
        returns: a simplified (ascii, lowercase) string
        """
        return unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').lower()

    def _fuzz(self, path, addition, child_rule=(lambda path: os.listdir(path)), min_sim=90):
        """
        path: a path-like object
        addition: a folder or file name
        """
        # find all children in directory and filter out some children.
        # get the score for each child
        # find the best score
        # find the child with the closest name
        # make sure child name isn't too different from desired name
        children = child_rule(path)
        print(children)
        scores = [fuzz.ratio(self._simplify(addition), self._simplify(child)) for child in children]
        best = max(scores)
        best_child = children[scores.index(best)]
        print(best, best_child, addition)
        assert best >= min_sim

        # return the full path to the child
        return join(path, best_child)

    def _fuzz_path(self, path, additions):
        # handle corner cases
        if len(additions) == 0: return path
        if len(additions) == 1: return self._fuzz(path, additions[0], min_sim=self.file_fuzz)

        folders, file = additions[:-1], additions[-1]

        for folder in folders:
            path = join(path, self._fuzz(
                path,
                folder,
                child_rule=self._filter_folders,
                min_sim=90))

        path = join(path, self._fuzz(
            path,
            file,
            child_rule=self._filter_files,
            min_sim=0))

        return path


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
