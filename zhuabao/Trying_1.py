import pcap
import dpkt
import urllib

def capt_data(eth_name="Realtek PCIe GbE Family Controller",packet_type=None):
    """
    捕获网卡数据包
    :param eth_name  网卡名，eg. eth0,eth3...
    :param p_type    日志捕获类型 1：sdk日志用例分析 2：目标域名过滤输出 3：原始数据包
    :return:
    """
    pc = pcap.pcap(eth_name)   #name parameter => interface name
    pc.setfilter("tcp")             #设置监听过滤
    print('atart capture ...')   
    if pc:                      #filter sentence
        for packet_time,packet_data in pc:
            pass

# packet_time  => packet receive time
# packet_data  => ethernet level data

    packet = dpkt.ethernet.Ethernet(packet_data)#二层数据报文嘛
    print ("SRC IP:%d.%d.%d.%d"%tuple(map(ord,list(packet.data.src))))
    print ("DST IP:%d.%d.%d.%d"%tuple(map(ord,list(packet.data.dst))))
    print ("SRC PORT:%s"%packet.data.data.sport)
    print ("DST PORT:%s"%packet.data.data.dport)
# 解包
def http_request_analyst(string):
        string = string[1:-1]
        method = string.split(" ")[0]
        print ("Method:",method)
        path = string.split(" ")[1]
        print ("Path:",urllib.unquote(path))
        protover = string.split(" ")[2].split("\\r\\n")[0]
        print ("Protocol Version:",protover)
        headers = string.split("\\r\\n\\r\\n")[0].split("\\r\\n")[1:]
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ("Header:")
        for header in headers:
                header = header.split(":")
                try:
                        hstr = "%s:%s"%(str(header[0]),str(header[1])) if header[0] not in ["Referer"] else "%s:%s:%s"%(str(header[0]),str(header[1]),str(header[2]))
                except Exception as ex:
                        print ("[*]",ex)
                        print (header)
                        input()
                print (hstr)
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ("Data:",string.split("\\r\\n")[-1])
# http解包
def http_response_analyst(string):
        string = string[1:-1]
        protover = string.split(" ")[0]
        print ("Protocol Version:",protover)
        status_code = string.split(" ")[1]
        print ("Response Code:",status_code)
        status_string = string.split(" ")[2].split("\\r\\n")[0]
        print ("Reposne String:",status_string)
        headers = string.split("\\r\\n\\r\\n")[0].split("\\r\\n")[1:]
        print (repr(headers))
        print (repr(string))
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ("Header:")
        for header in headers:
                header = header.split(":")
                try:
                        hstr = "%s:%s"%(str(header[0]),str(header[1])) if header[0] not in ["Referer"] else "%s:%s:%s"%(str(header[0]),str(header[1]),str(header[2]))
                except Exception as ex:
                        print ("[*]",ex)
                        print (header)
                        input()
                print (hstr)
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ("Data:",string.split("\\r\\n")[-1])

if __name__ == '__main__':
    capt_data("Realtek PCIe GbE Family Controller",1)
    http_request_analyst()
    http_response_analyst()
    print('my frist python file')
    