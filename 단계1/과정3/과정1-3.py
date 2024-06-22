with open("C:\Users\USER\Desktop\파이썬 프로그래밍 모음집\project-x-1-1\과정3\Mars_Base_Inventory_List.csv"," r") as csv_file:
    
List = []
ff = ''
kk = []
big = []
r = 0
while True:
    k = f.readline()
    if not k:
        break
    print(k)
    print('')
    List.append(k)
    ff = k.split(',')
    print(ff)
    kk.append(ff[-1])
    try:
        ff[-1] == float
        r = float(ff[-1])
        if r>0.7:
            big.append(k)
    except:
        continue

''''
for i in kk:
    if i==float:
        r=float(i)
        if r>0.7:
            big.append(i)
    else:
        continue
'''
#본격적 시작
print('')
print(kk)
s = sorted(kk)
print('')
print(s)
print('')
print(big)
print('끝')
#CSV 포맷
import csv
fi=open("C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/Mars_Base_Inventory_List.csv",'w')
for line in big:
    fi.write(line)
fi.close