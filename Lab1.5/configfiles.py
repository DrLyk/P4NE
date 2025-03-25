import os
import re


# Функция для извлечения IP-адресов и масок из лог-файлов в текущей директории
def extract_ips_from_logs():
    # Регулярное выражение для поиска строк, содержащих IP-адреса и маски
    ip_pattern = re.compile(r'ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)')
    unique_ips = set()

    # Получаем список всех файлов с расширением .log в текущей директории
    log_files = [f for f in os.listdir('.') if f.endswith(".log")]

    # Обрабатываем каждый найденный лог-файл
    for log_file in log_files:
        with open(log_file) as file:
                for line in file:
                    # Проверяем, соответствует ли строка шаблону IP-адреса
                    match = ip_pattern.search(line)
                    if match:
                        # Добавляем найденный IP-адрес и маску в множество
                        unique_ips.add(f"{match.group(1)} {match.group(2)}")

     # Выводим найденные уникальные IP-адреса и маски, отсортированные по значению
    for ip in sorted(unique_ips):
        print(ip)


# Запускаем функцию для обработки файлов в текущей директории
extract_ips_from_logs()