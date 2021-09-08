#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Christian Klinger",
    author_email='ck@novareto.de',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Tools for Integrating with DS",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='uvds_reha_tools',
    name='uvds_reha_tools',
    packages=find_packages(include=['uvds_reha_tools', 'uvds_reha_tools.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/goschtl/uvds_reha_tools',
    version='0.1.0',
    zip_safe=False,
)
