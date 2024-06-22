with open("C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/단계1/과정3/Mars_Base_Inventory_List.csv","r") as csvfile:
    sentence_list = []   #리스트 형식으로 넣기 위해
    sentence_list_sort = []   #인화성 지수로 분류하기 위해
    sentence_list_big = []   #인화성 0.7보다 높은 내용들 넣기
    csvfile.readline()   #첫번째 줄 건너뛰기
    while True:
        sentence = csvfile.readline().rstrip()
        if not sentence:
            break
        print(sentence)
        sentence_list.append(sentence)
    print()
    print()
    for i in sentence_list:
        x = list(i.split(','))
        sentence_list_sort.append(x)    
    sentence_list_sort.sort(key=lambda a: a[-1])
    sentence_list_sort.reverse()
    for i in sentence_list_sort:    
        if float(i[-1]) > 0.7:
            sentence_list_big.append(i)
    for item in sentence_list_big:
        print(','.join(item))
import csv   #csv파일로 저장 시작
csv_file_path = 'C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/단계1/과정3/Mars_Base_Inventory_danger.csv'
with open(csv_file_path,'w',newline='') as cf:
    writer = csv.writer(cf)
    for row in sentence_list_big:
        writer.writerow(row)

                 