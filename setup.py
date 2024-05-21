# install: pip install -e .
# test: python setup.py test

from setuptools import setup, find_packages

setup(
    name='mining_repositories',
    version='0.1',
    packages=find_packages(include=['mining_repositories', 'mining_repositories.*']),
    install_requires=[
        'PyGithub'
    ],
    tests_require=[
        'unittest'
    ],
    test_suite='tests',
    python_requires='>=3.6',
)
