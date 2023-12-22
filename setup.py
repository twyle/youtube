from setuptools import find_packages, setup
from pip._vendor import tomli

# For consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open('pyproject.toml', 'r') as f:
    VERSION = tomli.load(f)['tool']['commitizen']['version']

DESCRIPTION = 'A python library that wraps around the YouTube V3 API. You can use it find and manage YouTube resources including Videos, Playlists, Channels and Comments.'

key_words = [
    'youtube', 'youtube-api', 'youtube comments', 'youtube videos',
    'youtube channels', 'youtube comment thread', 'create youtube playlist'
]

install_requires = [
    'oryks-google-oauth',
    'pydantic',
    'pydantic-settings'
]

setup(
    name='oryks-youtube',
    packages=find_packages(
        include=[
            'youtube',
            'youtube.models',
            'youtube.schemas',
            'youtube.resources',
            'youtube.resources.search',
            'youtube.resources.video'
            'youtube.resources.channel',
            'youtube.resources.playlist',
            'youtube.resources.playlist_item',
            'youtube.resources.comment_thread'
        ]
    ),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    url='https://youtube-wrapper.readthedocs.io/en/latest/index.html',
    author='Lyle Okoth',
    author_email='lyceokoth@gmail.com',
    license='MIT',
    install_requires=install_requires,
    keywords=key_words,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent'
    ],
)
