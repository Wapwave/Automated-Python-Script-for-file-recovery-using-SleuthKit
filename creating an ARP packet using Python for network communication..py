target_ip = "192.168.1.1/24"
# IP Address for the destination
# create ARP packet
arp = ARP({% load pdst_tags %}=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp