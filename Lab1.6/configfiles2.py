import os
import re
import ipaddress


# Функция для проверки строки и извлечения IP-адреса и маски
# Возвращает объект ipaddress.IPv4Interface, если строка содержит IP-адрес, иначе None
def parse_ip_address(line):
    ip_pattern = re.compile(r'ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)')
    match = ip_pattern.search(line)
    if match:
        try:
            return ipaddress.IPv4Interface(f"{match.group(1)}/{match.group(2)}")
        except NoneIP:
            return None


# Функция для обработки всех конфигурационных файлов в текущей директории
def extract_ips_from_configs():
    unique_ips = set()  # Используем множество для хранения уникальных значений

    # Получаем список всех файлов с расширением .log в текущей директории
    config_files = [f for f in os.listdir('.') if f.endswith(".log")]

    # Обрабатываем каждый найденный конфигурационный файл
    for config_file in config_files:
            with open(config_file) as file:
                for line in file:
                    ip_interface = parse_ip_address(line)  # Классифицируем строку
                    if ip_interface:
                        unique_ips.add(str(ip_interface))


    # Выводим найденные уникальные IP-адреса и маски, отсортированные по значению

    print("Найденные IP-адреса и маски:")
    for ip in sorted(unique_ips):
        print(ip)


# Запускаем функцию для обработки файлов в текущей директории
extract_ips_from_configs()
