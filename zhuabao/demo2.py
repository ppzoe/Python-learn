import scapy.all as scapy
from scapy.layers.http import *
try:
    import scapy.all as scapy
except ImportError:
    import scapy
def parse_http_pcap(pcap_path):
    pcap_infos = list()
    packets = scapy.rdpcap(pcap_path)
    for p in packets:
        print ("----")
        # 判断是否包含某一层，用haslayer
        if p.haslayer("IP"):
            src_ip = p["IP"].src
            dst_ip = p["IP"].dst
            print ("sip: %s" % src_ip)
            print ("dip: %s" % dst_ip)
        if p.haslayer("TCP"):
            # 获取某一层的原始负载用.payload.original
            raw_http = p["TCP"].payload.original
            sport = p["TCP"].sport
            dport = p["TCP"].dport
            print ("sport: %s" % sport)
            print ("dport: %s" % dport)
            print ("raw_http:\n%s" % raw_http)
        if p.haslayer("HTTPRequest"):
            host = p["HTTPRequest"].Host
            uri = p["HTTPRequest"].Path
            # 直接获取提取好的字典形式的http数据用fields
            http_fields = p["HTTPRequest"].fields
            http_payload = p["HTTPRequest"].payload.fields
            print ("host: %s" % host)
            print ("uri: %s" % uri)
            print ("http_fields:\n%s" % http_fields)
            print ("http_payload:\n%s" % http_payload)

parse_http_pcap("pc1.pcap")

