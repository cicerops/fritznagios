import os

from setuptools import setup


def read(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as f:
        return f.read()


long_description = read("README.md")

setup(
    name="fritznagios",
    version="0.1.2",
    url="https://github.com/cicerops/fritznagios",
    author="Jan Hoffmann",
    author_email="jan.hoffmann@cicerops.de",
    description="Nagios/Icinga monitoring check program for FRITZ!Box devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=["any"],
    license="MIT",
    keywords="FRITZ!Box, AVM, fritzbox, fritz, Nagios, Icinga, monitoring, TR-064, UPnP",
    py_modules=["fritznagios"],
    entry_points={"console_scripts": ["fritznagios = fritznagios:main"]},
    python_requires=">=3.4",
    install_requires=["fritzconnection>=1,<2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Topic :: Communications",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Archiving",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
)
