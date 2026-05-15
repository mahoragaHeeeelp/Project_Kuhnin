# Вариант 5
# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые маски» 
# перенести в первый файл строки с нулевым четвертым октетом, а во второй — все остальные. 
# Посчитать количество полученных строк в каждом файле.

import re
from functools import partial

def extract_masks_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'Частоупотребимые\s+маски\s*\n(.*?)(?=\n\n|\nКоличество|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        masks_section = match.group(1)
        masks = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', masks_section)
        return masks
    return []

def has_zero_fourth_octet(mask):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.0$'
    return bool(re.match(pattern, mask))

masks = extract_masks_from_file('ip_address.txt')

zero_fourth_octet = list(filter(has_zero_fourth_octet, masks))
other_masks = list(filter(partial(lambda x, y: x not in y, y=zero_fourth_octet), masks))

print("строк с нулевым четвертым октетом: {len(zero_fourth_octet)}")
for mask in zero_fourth_octet:
    print(mask)

print("строк с ненулевым четвертым октетом: {len(other_masks)}")
for mask in other_masks:
    print(mask)
