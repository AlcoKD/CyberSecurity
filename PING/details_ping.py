from scapy.all import ls, IP

dest_ip="192.168.186.129"
ip_layer=IP(dst=dest_ip)
print(ls(ip_layer))
print("info = ", ip_layer.summary())
