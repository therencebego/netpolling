#! /usr/bin/python2.7
# -*- coding:Utf-8 -*-
from scapy.all import *
#from scapy.modules.nmap import *

class LocalScan:
    def __init__(self, name, net):
        self.net = net
        self.name = name

    def GetIpAndMac(self):
        ans, unans = arping("192.168.0.*")
        l = list()

        for elem in ans:
            l.append({"mac":elem[1].src, "ip":elem[1].psrc, "device": None, "os": None, "hostname":None, "route":None})
        return l

    def GetDevice(self):
        return

    def GetOS(self):
        return

    def GetHostName(self):
        return

    def GetRoute(self):
        return
