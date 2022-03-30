# Fritznagios

[![Status](https://img.shields.io/pypi/status/fritznagios.svg?style=flat-square)](https://pypi.org/project/fritznagios/)
[![License](https://img.shields.io/github/license/cicerops/fritznagios.svg?style=flat-square)](https://github.com/cicerops/fritznagios/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fritznagios.svg?style=flat-square)](https://pypi.org/project/fritznagios/)
[![Python versions](https://img.shields.io/pypi/pyversions/fritznagios.svg?style=flat-square)](https://pypi.org/project/fritznagios/)
[![Downloads](https://img.shields.io/pypi/dm/fritznagios.svg?style=flat-square)](https://pypi.org/project/fritznagios/)

## About

Nagios/Icinga monitoring check program for FRITZ!Box devices based on the
excellent [fritzconnection] module for maximum device coverage. It uses
the TR-064 protocol over [UPnP].

Icinga Exchange: https://exchange.icinga.com/tonke/fritznagios

[fritzconnection]: https://github.com/kbr/fritzconnection
[UPnP]: https://en.wikipedia.org/wiki/Universal_Plug_and_Play

## Setup

    python3 -m venv /opt/fritznagios
    /opt/fritznagios/bin/pip install git+https://github.com/cicerops/fritznagios

## Usage

    fritznagios --help

## Icinga 2

For integrating the check program into Icinga 2, you can use the
configuration files in the `icinga2` subdirectory. You can easily
acquire the files using:

    wget https://raw.githubusercontent.com/cicerops/fritznagios/main/icinga2/fritznagios-command.conf
    wget https://raw.githubusercontent.com/cicerops/fritznagios/main/icinga2/fritznagios-services.conf
    wget https://raw.githubusercontent.com/cicerops/fritznagios/main/icinga2/fritznagios-host.conf

## Development

Acquire sources:

    git clone https://github.com/cicerops/fritznagios
    cd fritznagios

Install program in development mode:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install --editable=.
