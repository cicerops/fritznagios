# -*- coding: utf-8; -*-

import os

from setuptools import setup


def read(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as f:
        return f.read()


long_description = read("README.rst")

setup(
    name="fritznagios",
    version="0.0.0",
    url="https://github.com/cicerops/fritznagios",
    author="Jan Hoffmann",
    author_email="jan.hoffmann@bergamsee.de",
    description="Monitoring sensor for Fritzboxes",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    platforms=["any"],
    license="MIT",
    keywords="",
    py_modules=["fritznagios"],
    entry_points={"console_scripts": ["fritznagios = fritznagios:main"]},
    python_requires=">=3.4",
    install_requires=["fritzconnection>=1,<2"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
