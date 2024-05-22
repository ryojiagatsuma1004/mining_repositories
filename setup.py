# install: pip install -e .
# test: python setup.py test

from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]


setup(
    name='mining_repositories',
    version='0.1',
    packages=find_packages(include=['mining_repositories', 'mining_repositories.*']),
    install_requires=parse_requirements('requirements.txt'),
    test_suite='tests',
    python_requires='>=3.6',
)
