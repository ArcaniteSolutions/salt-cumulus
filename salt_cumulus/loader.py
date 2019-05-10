import os


PKG_DIR = os.path.abspath(os.path.dirname(__file__))


def states_dirs():
    yield os.path.join(PKG_DIR, 'states')
