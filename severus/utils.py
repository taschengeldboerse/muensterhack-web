import os
import subprocess


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
