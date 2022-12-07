import time

from scapy.all import *

load_contrib('eigrp')

for i in range (0, 50):
    sendp(Ether()/IP(sr))