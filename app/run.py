from . import *

import os

import flask
from flask import Flask

from mistune import markdown as md
from m2r import convert as rst

from fuzzywuzzy import fuzz
import unicodedata

# from bs4 import BeautifulSoup

# html = markdown(some_html_string)
# text = ''.join(BeautifulSoup(html).findAll(text=True))

def list_folders(path):
    # get all folders
    folders = [x for x in os.listdir(path) if os.path.isdir(join(path, x))]

    #remove the src
    # remove hidden folders
    folders = list(filter(lambda x: True if x[0] != "." else False, folders))
    folders = list(filter(lambda x: True if x != "src" else False, folders))

    return folders

def list_files(path):
    # get all folders
    files = [x for x in os.listdir(path) if os.path.isfile(join(path, x))]

    # remove hidden folders
    files = list(filter(lambda x: True if x[0] != "." else False, files))

    return files

def simplify(string):
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
    string = string.lower()
    return string

def find_closest(target, samples):
    scores = list(map(lambda x: fuzz.ratio(target, x), samples))
    return max(zip(scores, samples), key=lambda x: x[0])

def fuzz_path(path, folders):
    for folder in folders:
        contents = list_folders(path)
        contents = dict(zip(map(simplify, contents), contents))

        score, name = find_closest(simplify(folder), contents.keys())
        assert score >= 90

        path = join(path, contents[name])

    return path

def fuzz_files(path, end):
    if not os.path.exists(join(path, end)):
        files = list_files(path)
        folders = list_folders(path)

        files = dict(zip(map(simplify, files), files))
        folders = dict(zip(map(simplify, folders), folders))

        assert len(folders) != 0 or len(files) != 0

        file_score = 0
        folder_score = 0

        if len(files) != 0:
            file_score, file  = find_closest(end, files.keys())
            file = files[file]
            end = file

        if len(folders) != 0:
            folder_score, folder = find_closest(end, folders.keys())
            end = folder
            folder = folders[folder]

        if len(folders) != 0 and len(folders) != 0:
            score, end = max([(file_score, file), (folder_score, folder)], key=lambda x: x[0])

        # make sure url isn't too far off from expected file
        # assert max([file_score, folder_score]) > 60

    return join(path, end)

def find_difference(base_path, addition):
    common = os.path.commonpath([base_path, addition])
    relative = addition[len(common):]
    print("\n\nbase: '{}'\nadd: '{}'\ncommon: '{}'\nrelative: '{}'\n\n".format(base_path, addition, common, relative))
    return "/index" if relative == "" else relative

def get_sections(path):
    """
    path: path-like object containing a directory
    returns: all the folders inside that path
    """
    folders = list_folders(path)
    return folders

def render_folder(env, sections, path, full_path):
    files = list_files(full_path)
    folders = list_folders(full_path)
    all = files + folders

    if len(files) == 1:
        return render_file(env, sections, join(full_path, files[0]))

    relatives = list(map(lambda x: find_difference(path, join(full_path, x)), all))
    all = list(zip(relatives, all, [""]*len(all)))

    return flask.render_template(
        "section.html",
        pages=all,
        section=os.path.basename(full_path),
        sections=sections,
        name=env.name,
        author=env.author,
        description=env.description,
    )

def render_file(env, sections, full_path):
    markup = {
        ".md": md,
        ".rst": rst
    }

    file, ext = os.path.splitext(full_path)
    with open(full_path, "r") as f:
        data = f.read()

    if ext in markup:
        page = markup[ext](data)
        return flask.render_template(
            "page.html",
            page=flask.Markup(page),
            sections=sections,
            name=env.name,
            author=env.author,
            description=env.description,
        )
    else:
        return flask.render_template(
            "file.html",
            file_name=os.path.basename(full_path),
            data=flask.Markup(data),
            sections=sections,
            name=env.name,
            author=env.author,
            description=env.description,
        )

def parse(path_list, env):
    path = env.project_path
    folders, end = path_list[:-1], path_list[-1]

    base_path = fuzz_path(path, folders)
    full_path = fuzz_files(base_path, end)

    sections = get_sections(base_path)
    relatives = list(map(lambda x: find_difference(path, join(base_path, x)), sections))
    sections = list(zip(relatives, sections))

    sections = [(find_difference(path, base_path), "← Back")] + sections

    if os.path.isdir(full_path): template = render_folder(env, sections, path, full_path)
    else: template = render_file(env, sections, full_path)

    return template

def run(args):
    # checking args
    assert len(args) == 0

    # setting up env
    env = auto_env()

    #starting the flask app
    app = Flask(__name__)

    @app.route('/index')
    @app.route('/')
    def root():
        meta([])
        nonlocal env
        sections = list(zip(
            map(lambda x: join("/", x), list_folders(env.project_path)),
            list_folders(env.project_path)
        ))
        return render_folder(env,
            sections,
            env.project_path,
            env.project_path
        )

    # path for building
    @app.route('/<path:page>')
    def route(page):
        meta([]) # build style for each request
        nonlocal env
        return parse(page.split("/"), env)

    @app.route('/src/<path:path>')
    def src(path):
        path = path.split("/")
        folders, end = path[:-1], path[-1]

        base_path = fuzz_path(join(env.project_path, "src"), folders)
        full_path = fuzz_files(base_path, end)

        return flask.send_file(full_path)

    app.run(debug=True)
