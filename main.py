import argparse

import app

parser = argparse.ArgumentParser()
parser.add_argument("command", type=str, help="the command to run")
command, args = parser.parse_known_args()


commands = {
    "init": app.init,
    "run": app.run,
    "configure": app.configure,
    "meta": app.meta
}

# this LOC tho
command = commands[command.command]

# TODO: When viewing a file make is show other folders 
# TODO: make the back button able to go back to the root
# TODO: make it so that static files work
# TODO: add docstrings

# BAM
if __name__ == "__main__":
    command(args)
