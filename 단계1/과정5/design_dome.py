import numpy as np
arr1 = np.genfromtxt('C:/Users/USER/AppData/Local/Temp/02bb6f61-2819-40d1-a98b-77939c3a11db_uqstnd28f32a5-62a5-4456-b1f8-77b64b573a8d_dup_1713172143829_문제5 (1).zip.1db/mars_base_main_parts-001.csv',delimiter=',',dtype=None,names=True,encoding="utf-8")
arr2 = np.genfromtxt('C:/Users/USER/AppData/Local/Temp/895380c1-df14-45e2-b816-89adc305cacf_uqstnd28f32a5-62a5-4456-b1f8-77b64b573a8d_dup_1713172143829_문제5 (1).zip.acf/mars_base_main_parts-002.csv',delimiter=',',dtype=None,names=True,encoding="utf-8")
arr3 = np.genfromtxt('C:/Users/USER/AppData/Local/Temp/98e99634-a630-4755-9d3c-07065509c899_uqstnd28f32a5-62a5-4456-b1f8-77b64b573a8d_dup_1713172143829_문제5 (1).zip.899/mars_base_main_parts-003.csv',delimiter=',',dtype=None,names=True,encoding="utf-8")
parts = np.concatenate([arr1,arr2,arr3])
parts_sum = {}

for part, strength in parts:
    if part in parts_sum:
        parts_sum[part] += strength
    else:
        parts_sum[part] = strength


parts_average = {}
for part,strength in parts_sum.items():
    parts_average[part] = strength//3

average_small = {}
for part,strength in parts_average.items():
    if strength < 50:
        average_small[part] = strength
    else:
        continue
print(average_small)

import csv

csv_file_path = 'C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/과정5/parts_to_work_on.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Part', 'Strength']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()'/'

    for part, strength in average_small.items():
        writer.writerow({'Part': part, 'Strength': strength})

