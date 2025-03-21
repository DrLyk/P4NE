from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        addr = random.randint(0x0B000000, 0xDF000000)
        mask = random.randint(8, 24)
        IPv4Network.__init__(self, (addr, mask), strict=False)
    def regular(self):
        return not (self.is_private or self.is_link_local or self.is_multicast)

networks = [IPv4RandomNetwork() for _ in range(50)]

sorted_networks = sorted(networks, key=lambda net: (net.prefixlen, net.network_address))

for net in sorted_networks:
    print(net)