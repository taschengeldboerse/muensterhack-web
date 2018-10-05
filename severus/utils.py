import os
import subprocess

from severus.db import db, Task, User, StandardTask


def get_version():
    version = os.getenv('SEVERUS_VERSION')
    if version:
        return version
    try:
        branch = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            stdout=subprocess.PIPE, encoding='utf8').stdout.strip()
        commit = subprocess.run(
            ['git', 'describe', '--always'],
            stdout=subprocess.PIPE, encoding='utf8').stdout.strip()
        return '-'.join([branch, commit])
    except FileNotFoundError:
        return 'unknown-dev-build'


def initialize_database():
    db.create_tables([Task, User, StandardTask], safe=True)
