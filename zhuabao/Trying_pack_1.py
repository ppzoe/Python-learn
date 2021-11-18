# 1
import pcap, dpkt
import re, threading, requests
  
__black_ip = ['103.224.249.123', '203.66.1.212']
 
# 抓包：param1 eth_name 网卡名，如：eth0,eth3。 param2 p_type 日志捕获类型 1：sdk日志用例分析 2：目标域名过滤输出 3：原始数据包
def catch_pack(eth_name="enp5s0", packet_type=None):
    sniffer = pcap.pcap(eth_name)
    sniffer.setfilter("tcp")            # 只抓取TCP包
    # sniffer.setfilter('tcp port 80')  # 设置监听过滤器
    print("开始监控 ---")
    if sniffer:
        for packet_time, packet_data in sniffer:  # packet_time为收到的时间，packet_data为收到的数据
            th = threading.Thread(target=check_pack, args=(packet_time, packet_data, packet_type))
            th.setDaemon(True)
            th.start()

  
# 解包
def check_pack(packet_time, packet_data, packet_type):
    packet = dpkt.ethernet.Ethernet(packet_data)
    # 判断是否HTTP协议javascript:;
    try:
        m_tips = packet.data.data.data[:3]
    except:
        return False
    if m_tips != 'GET' and m_tips != 'POS': return False
  
    # 取回头信息
    tmp = get_header(packet, packet_time)
    if not tmp: return False
    print ("tmp===>", tmp)
    # self.input_database(tmp)
  
# 取header数据
def get_header(packet, packet_time):
    if not packet: return False
    tmp = {}
  
    # 获取基础头信息
    tmp['dst'] = "%d.%d.%d.%d" % tuple(map(ord, list(packet.data.dst)))
    if tmp['dst'] in __black_ip: return False
    tmp['src'] = "%d.%d.%d.%d" % tuple(map(ord, list(packet.data.src)))
    tmp['time'] = packet_time
    tmp['dport'] = packet.data.data.dport
    tmp['sport'] = packet.data.data.sport
    # if not self.ip_exists(tmp['dst']): self.input_ip(tmp['dst'])
  
    # 截取前1024个字符
    t = packet.data.data.data[:1024]
  
    # 获取host,uri,referer,method
    o = re.search('(GET|POST)\s+(.+)\s+HTTP(.|\n)+Host:\s+(.+)\r(.|\n)+Referer:\s+(.+)\r', t)
    if not o: return False
    o1 = o.groups()
    if len(o1) < 6: return False
    tmp['method'] = o1[0]
    tmp['host'] = o1[3]
    tmp['uri'] = o1[1]
    tmp['referer'] = o1[5]
    # if self.is_exists(tmp['host'],tmp['dport']): return False
    return tmp
  
# if __name__ == "__main__":
#     catch_pack("eth0", 1)
