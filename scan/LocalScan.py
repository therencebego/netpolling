#! /usr/bin/python2.7
# -*- coding:Utf-8 -*-
from scapy.all import *
#from scapy.modules.nmap import *
"""@package docstring
This file contain the class : LocalScan
"""

class LocalScan:
    """LocalScan :
        - net : this variable contain the pattern of the network (ex : 192.168.0.* or 10.8.12.* for netmask /24)
        - name : this variable contain the name for identify the scan in the database
    """
    def __init__(self, name, net):
        self.net = net
        self.name = name

    def GetIpAndMac(self):
        """GetIpAndMac :
        This method scans the network to get adresses ip and mac of all machines
        """
        ans, unans = arping(self.net)
        l = list()

        for elem in ans:
            l.append({"mac": elem[1].src, "ip": elem[1].psrc, "device": None, "os": None, "hostname": None, "route": None})
        return l

    def GetDevice(self):
        """GetDevice :
        """
        return

    def GetOS(self):
        """GetOS :
        """
        return

    def GetHostName(self):
        """GetHostName :
        """
        return

    def GetRoute(self):
        """GetRoute :
        """
        return
