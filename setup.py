from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='insajderi_crawler',
    packages=['crawler'],
    description="Python crawler that crawls the rss feed(s) of an Albanian portal",
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version='0.0.2',
    url='https://github.com/tot98git/crawler',
    author='Toti Kadriu',
    author_email='toti.kadriu@gmail.com',
    keywords=['crawler', 'albanian', 'rss'],
    python_requires='>=3'
)