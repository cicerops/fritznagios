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
from fritzconnection.core.fritzconnection import (
    FritzConnection,
    FRITZ_IP_ADDRESS,
    FRITZ_TCP_PORT,
)
import math
import ipaddress
import datetime
import argparse
import os


class Nagios:
    def __init__(self):
        self.fs = None
        self.args = self.get_cli_arguments()
        self.state = 'OK'

    def set_fs(self):
        self.fs = self.get_instance(FritzStatus, self.args)

    def main(self):
        modes = ['ip', 'uptime', 'bytes', 'bitrate']
        if self.args.mode == 'uptime':
            if not self.args.password:
                print("Exit: password required.")
                exit()
        if self.args.warning:
            try:
                self.args.warning = int(self.args.warning)
            except:
                print("Exit: -w Warning Level as Int required.")
                exit()
        if self.args.critical:
            try:
                self.args.critical = int(self.args.critical)
            except:
                print("Error: -c Critical Level as Int required.")
                exit()
        if self.args.mode not in modes:
            print('Exit: -m Requires something like %s' % modes)
        else:
            self.set_fs()
            if self.args.mode in modes:
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

    def get_instance(self, cls, args):
        return cls(
            address=args.address,
            port=args.port,
            user=args.username,
            password=args.password,
            use_tls=args.encrypt,
        )

    def get_cli_arguments(self, scan_additional_arguments=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ip-address',
                            nargs='?', default=FRITZ_IP_ADDRESS, const=None,
                            dest='address',
                            help='Specify ip-address of the FritzBox to connect to.'
                                 'Default: %s' % FRITZ_IP_ADDRESS)
        parser.add_argument('--port',
                            nargs='?', default=None, const=None,
                            help='Port of the FritzBox to connect to. '
                                 'Default: %s' % FRITZ_TCP_PORT)
        parser.add_argument('-u', '--username',
                            nargs='?', default=os.getenv('FRITZ_USERNAME', None),
                            help='Fritzbox authentication username')
        parser.add_argument('-p', '--password',
                            nargs='?', default=os.getenv('FRITZ_PASSWORD', None),
                            help='Fritzbox authentication password')
        parser.add_argument('-e', '--encrypt',
                            nargs='?', default=False, const=True,
                            help='use secure connection')
        parser.add_argument('-mode', '--mode',
                            nargs='?', default="bitrate", const=True,
                            help='set check mode')
        parser.add_argument('-w', '--warning',
                            nargs='?', default=False, const=True,
                            help='set warning level')
        parser.add_argument('-c', '--critical',
                            nargs='?', default=False, const=True,
                            help='set critical level')
        #if scan_additional_arguments:
        #    scan_additional_arguments(parser)
        args = parser.parse_args()
        return args


if __name__ == "__main__":
    nagios = Nagios()
    nagios.main()
