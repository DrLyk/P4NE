import os
import re
import ipaddress
from flask import Flask, jsonify

app = Flask(__name__)

# Функция для проверки строки и извлечения IP-адреса и маски
# Возвращает объект ipaddress.IPv4Interface, если строка содержит IP-адрес, иначе None
def parse_ip_address(line):
    ip_pattern = re.compile(r'ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)')
    match = ip_pattern.search(line)
    if match:
        return ipaddress.IPv4Interface(f"{match.group(1)}/{match.group(2)}")
    else:
        return None


# Функция для получения всех конфигурационных файлов в текущей директории
def get_config_files():
    return [f for f in os.listdir('.') if f.endswith(".log")]

# Функция для извлечения IP-адресов из файлов конкретного хоста
def extract_ips_for_host(hostname):
    filename = f"{hostname}.log"
    unique_ips = set()
    if os.path.exists(filename):
        with open(filename) as file:
            for line in file:
                ip_interface = parse_ip_address(line)
                if ip_interface:
                    unique_ips.add(str(ip_interface))
    return list(unique_ips)

# Корневой маршрут - справка
@app.route('/')
def home():
    return "<p>Используйте <a href=../configs>/configs</a> для списка хостов и /config/&lt;hostname&gt; для IP-адресов конкретного хоста.</p>"

# Маршрут для получения списка хостов
@app.route('/configs')
def configs():
    config_files = get_config_files()
    hostnames = [os.path.splitext(f)[0] for f in config_files]
    links = ""
    for hostname in hostnames:
        links += f"<p><a href='/config/{hostname}'>{hostname}</a></p>"
    return links

# Маршрут для получения IP-адресов конкретного хоста
@app.route('/config/<hostname>')
def config(hostname):
    ips = extract_ips_for_host(hostname)
    return jsonify(ips)


@app.get('/favicon.ico')
def Icon():
    return '<head> <link rel="icon" href="favicon.ico" /> </head>'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)