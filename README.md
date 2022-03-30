# Fritznagios

## About

Nagios/Icinga monitoring check program for FRITZ!Box based on the excellent
[fritzconnection](https://github.com/kbr/fritzconnection) module.

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