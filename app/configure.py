from . import *

import os

def join(*args):
    path = args[0]
    for arg in args[1:]:
        path = os.path.join(path, arg)
    return path    

def get_path(path, correct_path):
    while True:
        if correct_path(path): return path
        else:
            new_path = os.path.split(path)[0]
            assert new_path != path
            path = new_path

def get_veritable_path():
    veritable_path = join(os.getcwd(), __file__)
    def correct_path(path):
        return os.path.split(path)[1] == "veritable"
    return get_path(veritable_path, correct_path)

def get_project_path():
    project_path = os.getcwd()
    def correct_path(path):
        return os.path.isdir(join(path, ".veritable"))
    return get_path(project_path, correct_path)

class Env:
    def __init__(self, veritable_path, project_path):
        self.veritable_path = veritable_path
        self.project_path = project_path
        self.name = self.get_config("NAME")
        self.author = self.get_config("AUTHOR")
        self.description = self.get_config("DESCRIPTION")

    def get_config(self, file):
        with open(join(self.project_path, ".veritable", file), "r") as f:
            return " ".join(f.read().split())

    def set_config(self, file, value):
        with open((join(self.project_path, ".veritable", file)), "w") as f:
            f.write(value)

def auto_env():
    veritable_path = get_veritable_path()
    project_path = get_project_path()
    env = Env(veritable_path, project_path)
    return env

def configure(args):
    assert len(args) == 1
    variable = args[0]

    env = auto_env()

    valid_variables = [
        "NAME",
        "AUTHOR",
        "DESCRIPTION"
    ]
    assert variable in valid_variables

    env = auto_env()

    print("{} is already configured as '{}'".format(variable, env.get_config(variable)))
    if input("Would you like to change this? (y/n): ") == "y":
        env.set_config(variable, input("Project {}: ".format(variable)))
        print("{} has been updated".format(variable))
    else:
        print("{} has not been updated".format(variable))
