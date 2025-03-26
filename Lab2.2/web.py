import os
import re
import ipaddress
from flask import Flask, send_from_directory

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

# Генерация HTML списка ссылок для всех хостов
def generate_host_links(hostnames):
    return "".join(f"<li><a href='/config/{hostname}'>{hostname}</a></li>" for hostname in hostnames)


# Корневой маршрут - справка
@app.route('/')
def home():
    # Формируем ссылки для каждого хоста
    hostnames = [os.path.splitext(f)[0] for f in get_config_files()]
    links = generate_host_links(hostnames[:3])
    return f"""<head><title>IPs</title></head>
    <p>Используйте <a href=../configs>Полный перечень хостов</a> для просмотра всех хостов</p>
    <p>Перейдите по ссылке: /config/&lt;hostname&gt для просмотра IP-адресов конкретного хоста ;</p>
    <p>Или выберете из списка первых 3х хостов:</p>
    <ol>{links}</ol>
    """

# Маршрут для получения списка хостов
@app.route('/configs')
def configs():
    hostnames = [os.path.splitext(f)[0] for f in get_config_files()]
    links = generate_host_links(hostnames)
    return f"""<head><title>IPs</title></head>
    <ol>{links}</ol>"""

# Маршрут для получения IP-адресов конкретного хоста
@app.route('/config/<hostname>')
def config(hostname):
    ips = extract_ips_for_host(hostname)
    return  f"""<head>
    <title>IP-адреса для {hostname}</title>
</head>
<body>
    <h3>IP-адреса для {hostname}:</h3>
    <ol>
        {''.join([f'<li>{ip}</li>' for ip in ips])}
    </ol>
</body>"""


@app.get('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/x-icon')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)