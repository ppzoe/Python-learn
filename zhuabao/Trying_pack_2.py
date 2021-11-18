# 2
try:
    import scapy.all as scapy
except ImportError:
    import scapy
from scapy.utils import PcapReader
 
packets = scapy.rdpcap('test.pcap')
for data in packets:
    if 'UDP' in data:
        s = repr(data)
        print(data['UDP'].sport)
        break