import argparse
import shutil
import os

parser = argparse.ArgumentParser()
parser.add_argument("command", type=str, help='the command to run')
args, uargs = parser.parse_known_args()

PROJECT_PATH = os.getcwd()
SELF_PATH = os.path.dirname(os.path.abspath(__file__))

# assert os.path.isdir(os.path.join(PROJECT_PATH, ".veritable/"))

def new(args):
    assert len(args) == 1

    project_name = args[0]

    shutil.copytree(
        os.path.join(SELF_PATH, "base"),
        os.path.join(PROJECT_PATH, project_name)
    )

def run(args):
    pass

def bind(args):
    assert len(args) == 2

    variable = args[0]
    value = args[1]

    index = None

    with open(os.path.join(PROJECT_PATH, ".veritable/.config"), "r") as config:
        data = config.readlines()

    for i, line in enumerate(data):
        if line.split("=")[0] == variable:
            index = i
            break

    if index is not None:
        data[i] = variable + "=" + value + "\n"
    else:
        data.append(variable + "=" + value + "\n")

    with open(os.path.join(PROJECT_PATH, ".veritable/.config"), "w") as config:
        config.writelines(data)

def recompile(): pass

if args.command == "new": new(uargs)
if args.command == "run": run(uargs)
if args.command == "bind": bind(uargs)
if args.command == "recompile": recompile(uargs)
