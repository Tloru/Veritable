from . import *

from sass import compile as sass

def meta(args):
    assert len(args) == 0
    env = auto_env()

    # compile stylesheet
    styles = join(env.veritable_path, "app", "static", "styles")
    data = sass(filename=join(styles, "styles.sass"))
    with open(join(styles, "styles.css"), "w") as f: f.write(data)

    # rename folder structure
    # TODO: rename folder structure

    print("Successfully performed all meta tasks")
