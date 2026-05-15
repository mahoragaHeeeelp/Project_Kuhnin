# Вариант 5
# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые маски» 
# перенести в первый файл строки с нулевым четвертым октетом, а во второй — все остальные. 
# Посчитать количество полученных строк в каждом файле.

import re

file_name = 'ip_address.txt'
text = open(file_name, encoding='utf-8').read()

match = re.search(r'Частоупотребимые\s+маски\s*\n(.*?)(?=\n\S)', text, re.DOTALL)
content = match.group(1) if match else ""

all_ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)

zero_octet_ips = list(filter(lambda ip: ip.endswith('.0'), all_ips))
other_ips = list(filter(lambda ip: not ip.endswith('.0'), all_ips))

print(f"Количество строк с нулевым четвертым октетом: {len(zero_octet_ips)}")
print('\n'.join(zero_octet_ips))

print(f"\nКоличество строк с ненулевым четвертым октетом: {len(other_ips)}")
print('\n'.join(other_ips))
