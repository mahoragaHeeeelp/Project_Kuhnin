# Вариант 5
# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые маски» 
# перенести в первый файл строки с нулевым четвертым октетом, а во второй — все остальные. 
# Посчитать количество полученных строк в каждом файле.

import re

with open('ip_address.txt', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'Частоупотребимые\s+маски\s*\n(.*?)(?=\nКоличество|\Z)', text, re.DOTALL)
content = match.group(1) if match else ""
all_ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)

zero_ips = list(filter(lambda ip: ip.endswith('.0'), all_ips))
other_ips = list(filter(lambda ip: not ip.endswith('.0'), all_ips))

with open('first_file.txt', 'w', encoding='utf-8') as f1:
    f1.write('\n'.join(zero_ips) + f'\nКоличество строк: {len(zero_ips)}')

with open('second_file.txt', 'w', encoding='utf-8') as f2:
    f2.write('\n'.join(other_ips) + f'\nКоличество строк: {len(other_ips)}')
