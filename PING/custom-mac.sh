sudo ip link set dev eth0 down
sudo ip link set dev eth0 address 00:11:22:33:44:55
sudo ip link set dev eth0 up
#
#permanent change:
#
#nmcli connection modify <nome-connessione> ethernet.cloned-mac-address 00:11:22:33:44:55
#inmcli connection down <nome-connessione>
#nmcli connection up <nome-connessione>
#nmcli connection show
