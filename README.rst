###########
Fritznagios
###########


*****
Setup
*****

::

    pip install git+https://github.com/cicerops/fritznagios

For integrating into Icinga 2, you can use the ``fritznagios-icinga2.conf``
command configuration file. You can easily acquire it using::

    wget https://raw.githubusercontent.com/cicerops/fritznagios/main/fritznagios-icinga2.conf


*****
Usage
*****

::

    fritznagios --help



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
