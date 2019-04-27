from . import *

import os

import flask

from mistune import markdown as md
from m2r import convert as rst

from fuzzywuzzy import fuzz
import unicodedata

def simplify(string):
    """string: a str object"""
    return unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').lower()

def find_difference(base_path, addition):
    common = os.path.commonpath([base_path, addition])
    relative = addition[len(common):]
    return "/" if relative == "" else relative

def list_folders(vignore, path):
    # get all folders
    folders = [x for x in os.listdir(path) if os.path.isdir(join(path, x))]
    folders = list(filter(vignore, folders))
    folders = list(filter(lambda x: False if x == "src" else True, folders))

    return folders

def list_files(vignore, path):
    # get all folders
    # remove hidden files
    files = [x for x in os.listdir(path) if os.path.isfile(join(path, x))]
    files = list(filter(vignore, files))

    return files

def find_closest(target, samples):
    scores = list(map(lambda x: fuzz.ratio(target, x), samples))
    return max(zip(scores, samples), key=lambda x: x[0])

def fuzz_path(path, folders, vignore):
    for folder in folders:
        contents = list_folders(vignore, path)
        contents = dict(zip(map(simplify, contents), contents))

        score, name = find_closest(simplify(folder), contents.keys())
        assert score >= 90

        path = join(path, contents[name])

    return path

def fuzz_files(path, end, vignore):
    if not os.path.exists(join(path, end)):
        files = list_files(vignore, path)
        folders = list_folders(vignore, path)

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

        if len(folders) != 0 and len(files) != 0:
            score, end = max([(file_score, file), (folder_score, folder)], key=lambda x: x[0])

        # make sure url isn't too far off from expected file
        # assert max([file_score, folder_score]) > 60

    return join(path, end)

def render_folder(env, sections, path, full_path):
    files = list_files(env.vignore, full_path)
    folders = list_folders(env.vignore, full_path)
    all = files + folders

    index = list(filter(lambda x: os.path.splitext(x)[0] == "index", files))

    if len(index) != 1: index = None
    else: index = index[0]

    if len(files) == 1 and len(folders) == 0 or index is not None:
        file = index if index is not None else files[0]
        return render_file(env, sections, join(full_path, file))

    relatives = list(map(lambda x: find_difference(path, join(full_path, x)), all))
    all = list(zip(relatives, all))

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
        page = flask.Markup(markup[ext](data))
    else:
        page = flask.Markup("<pre>\n<code>{}\n</code></pre>".format(flask.escape(data)))

    return flask.render_template(
        "page.html",
        page=page,
        sections=sections,
        name=env.name,
        author=env.author,
        description=env.description,
    )

def parse(path_list, env):
    path = env.project_path
    folders, end = path_list[:-1], path_list[-1]

    base_path = fuzz_path(path, folders, env.vignore)
    full_path = fuzz_files(base_path, end, env.vignore)

    sections = list_folders(env.vignore, base_path)
    relatives = list(map(lambda x: find_difference(path, join(base_path, x)), sections))
    sections = list(zip(relatives, sections))

    if path_list != [""]: sections = [(find_difference(path, base_path), "← Back")] + sections

    if os.path.isdir(full_path): template = render_folder(env, sections, path, full_path)
    else: template = render_file(env, sections, full_path)

    return template
