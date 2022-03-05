###########
Fritznagios
###########


*****
Setup
*****

::

    pip install git+https://github.com/cicerops/fritznagios


*****
Usage
*****

::

    fritznagios --help

For integrating into Icinga 2, you can use the ``fritznagios-icinga2.conf``
command configuration file.



***********
Development
***********

Acquire sources::

    git clone https://github.com/cicerops/fritznagios
    cd fritznagios

Install program in development mode::

    python3 -m venv .venv
    source .venv/bin/activate
    pip install --editable=.
