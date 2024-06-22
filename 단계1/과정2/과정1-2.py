import json
f=open('C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/mission_computer_main.log','r')
k=[]
r=[]
dic_k={}

while True:
    line=f.readline()
    if not line:
        break
    linecut=line.split(',',1)
    print('시간:',linecut[0])
    print('내용:',linecut[1])
#역순으로 정렬하기
    k.append(linecut[0])
    r.append(linecut[1])
kk=k[::-1]
rr=r[::-1]
print('')
print('역순으로 출력하기')
print('')
for i in range(len(kk)):
    print(kk[i])
    print(rr[i])
print('')
print('')

#리스트->딕셔너리 및 json 파일 형식
def write_json(infile_path,outfile_path):
    with open(infile_path,'r') as infile:
        while True:
            line=infile.readline()
            if not line:
                break
            linecut=line.split(',')
            dic_k[linecut[0]]=linecut[2].strip()
    with open(outfile_path,'w') as outfile:
            json.dump(dic_k,outfile,indent=2)
write_json('C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/mission_computer_main.log','C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/mission_computer_main.json')   


    
