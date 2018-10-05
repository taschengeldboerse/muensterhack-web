from flask import Flask

from severus.utils import get_version


app = Flask('severus')


@app.route('/')
def root():
    return get_version()
