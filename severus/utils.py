import logging
import os
import subprocess
from functools import lru_cache

import requests
from geopy import distance


logger = logging.getLogger(__name__)


# Use Lambertikirche as default distance
DEFAULT_LATLON = (51.9628967, 7.628879643)


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


@lru_cache(maxsize=1024)
def get_latlon(address):
    resp = requests.get(
        'https://nominatim.openstreetmap.org/search?format=json&q=' + address,
        headers={
            'User-Agent': 'taschengeldboerse.io via python-requests',
        },
    )
    data = resp.json()
    try:
        return float(data[0]['lat']), float(data[0]['lon'])
    except IndexError:
        logger.warning(
            "Nominatim did not return any places for %s, using default latlon",
            address)
        return DEFAULT_LATLON


def get_distance(latlon1, latlon2):
    return distance.distance(latlon1, latlon2).m
