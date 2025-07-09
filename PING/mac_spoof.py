from scapy.all import Ether, ARP, srp, IP

if __name__=="__main__":
    broadcast="ff:ff:ff:ff:ff:ff"
    ether_layer=Ether(dst=broadcast, src="aa:bb:cc:dd:ee:ff")
    ip_layer=IP(src="192.168.186.20")
    ip_range="192.168.186.1/24"
    arp_layer=ARP(pdst=ip_range)
    packet=ether_layer/arp_layer/ip_layer
    ans,unans=srp(packet,iface="eth0",timeout=2)
    for snd, rcv in ans :
        ip=rcv[ARP].psrc
        mac=rcv[Ether].src
        print("IP = ", ip, " MAC = ", mac)