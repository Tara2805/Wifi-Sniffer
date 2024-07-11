from scapy.all import *
from scapy.layers.dot11 import Dot11ProbeReq

interface = 'wlan0'
probeReqs = []

def sniffProbes(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
        if netName not in probeReqs:
            probeReqs.append(netName)
            print(f'[+] Detected New Probe Request: {netName}')

sniff(iface=interface, prn=sniffProbes)

