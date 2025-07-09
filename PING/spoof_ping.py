
from scapy.all import ICMP, IP, sr

if __name__=="__main__":
    src_ip="192.168.186.5" ## sorgente IP spoofed
    dest_ip='192.168.186.129' # destionazione IP
    ip_layer=IP(src=src_ip, dst=dest_ip)
    print(ip_layer.show())
    icmp_req=ICMP(id=100)
    packet=ip_layer/icmp_req
    print(packet)
    response,_=sr(packet,iface="eth0")
    #print(response, ". ", _ )
    if response:
        response.show()