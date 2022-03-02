"""
fritznagios.py

Module for Nagios to query the FritzBox API for available services and actions.
CLI interface.

This module is depends on the FritzConnection package.
https://github.com/kbr/fritzconnection
License: MIT (https://opensource.org/licenses/MIT)
Author: Klaus Bremer
Edited by: Jan Hoffmann
"""

from fritzconnection.core.exceptions import FritzServiceError, FritzActionError
from fritzconnection.lib.fritzstatus import FritzStatus
from utils import get_cli_arguments, get_instance
import math
import ipaddress
import datetime


class Nagios:
    def __init__(self):
        self.args = get_cli_arguments()
        self.fs = get_instance(FritzStatus, self.args)
        self.state = 'OK'

    def main(self):
        modes = ['ip', 'uptime', 'bytes', 'bitrate']
        if not self.args.password:
            print("Exit: password required.")
            exit()
        if not self.args.warning:
            print("Exit: -w Warning Level required.")
            exit()
        try:
            self.args.warning = int(self.args.warning)
        except:
            print("Exit: -w Warning Level as Int required.")
            exit()
        if not self.args.critical:
            print("Exit: -c Critical Level required.")
            exit()
        try:
            self.args.critical = int(self.args.critical)
        except:
            print("Error: -c Critical Level as Int required.")
            exit()
        if not self.args.mode:
            print("Exit: -m Mode required.")
            exit()
        if not self.args.mode in modes:
            print('Exit: -m Requires something like %s' % modes)
            exit()
        else:
            fun = getattr(Nagios, self.args.mode)
            fun(self)

    def uptime(self):
        device_uptime = self.get_information('device_uptime')
        connection_uptime = self.get_information('connection_uptime')
        device_uptime = str(datetime.timedelta(seconds=device_uptime))
        connection_uptime = str(datetime.timedelta(seconds=connection_uptime))
        print(self.state + ' - Uptime: %s ConnectionUptime: %s' % (device_uptime, connection_uptime))

    def bytes(self):
        bytes_sent = self.get_information('bytes_sent')
        bytes_received = self.get_information('bytes_received')
        bytes_sent = bytes_sent/1000
        bytes_received = bytes_received/1000
        levels = 'KB'
        levelr = 'KB'
        if bytes_sent > 1024:
            bytes_sent = round(bytes_sent/1000, 2)
            levels = 'MB'
        if bytes_sent > 1024:
            bytes_sent = round(bytes_sent/1000, 2)
            levels = 'GB'
        if bytes_received > 1024:
            bytes_received = round(bytes_received/1000, 2)
            levelr = 'MB'
        if bytes_received > 1024:
            bytes_received = round(bytes_received/1000, 2)
            levelr = 'GB'
        print(self.state + ' - received:%s' % bytes_received + levelr + ' sent:%s' % bytes_sent + levels)

    def ip(self):
        counter = 0
        ipv4 = False
        ipv6 = False

        ipv4 = self.get_information('external_ip')
        ipv6 = self.get_information('external_ipv6')

        if ipv4:
            ipv4 = ipaddress.ip_address(ipv4)
            counter += 1
        if ipv6:
            ipv6 = ipaddress.ip_address(ipv6)
            counter += 1

        self.set_state(counter)

        if ipv4 and ipv6:
            print(self.state + ' - IPv4: %s, IPv6: %s' % (ipv4, ipv6))
        elif ipv4:
            print(self.state + ' - IPv4: %s' % ipv4)
        elif ipv6:
            print(self.state + ' - IPv6: %s' % ipv6)
        else:
            print(self.state + ' - No IP Address.')

    def bitrate(self):
        max_bit_rate = self.get_information('max_bit_rate')
        str_max_bit_rate = self.get_information('str_max_bit_rate')
        value = int(math.ceil(float(max_bit_rate[1]/1000000)))
        self.set_state(value)
        print(self.state + ' - DownlinkBitRate: %s UplinkBitRate: %s' % (str_max_bit_rate[1], str_max_bit_rate[0]))

    def get_information(self, attribute):
        try:
            information = getattr(self.fs, attribute)
        except (FritzServiceError, FritzActionError):
            information = f'unsupported attribute "{attribute}"'
        return information

    def set_state(self, value):
        if self.args.warning > value:
            self.state = 'WARNING'
        if self.args.critical > value:
            self.state = 'CRITICAL'


if __name__ == "__main__":
    nagios = Nagios()
    nagios.main()
