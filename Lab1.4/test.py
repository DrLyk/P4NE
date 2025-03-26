import random
from ipaddress import IPv4Address

class IPv4RandomNetwork:
    def __init__(self):
        # Генерация случайного IP-адреса в диапазоне от 11.0.0.0 до 223.0.0.0
        self.addr = random.randint(0x0B000000, 0xDF000000)
        # Генерация случайной маски сети от /8 до /24
        self.mask = random.randint(8, 24)
#        self.ip = IPv4Address(self.addr)

 #  def __repr__(self):
  #      # Возвращаем строку с IP-адресом и маской (например, 192.168.1.0/24)
   #     return f"{self.ip}/{self.mask}"
n1=IPv4RandomNetwork()
# Генерация 50 случайных сетей с IP и масками
networks = [IPv4RandomNetwork() for _ in range(50)]

# Сортировка сначала по маске, затем по IP-адресу
sorted_networks = sorted(networks, key=lambda net: (net.mask, net.addr))

# Выводим результат
for net in sorted_networks:
    print(net)