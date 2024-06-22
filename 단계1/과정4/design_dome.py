#전역변수 설정
material=''; weight=0; thickness=0; area=0; diameter=0;
#본 코딩
def sphere_area(diameter,material='유리',thickness=1):
    try:
        if m=='유리':
            weight=2.4  
        elif m=='알루미늄':
            weight=2.7
        elif m=='탄소강':
            weight=2.7
    except:
        print('잘못된 재질입니다')
    return '재질==>%s , 지름==>%d ,두께==>%d , 면적==>%f , 무게==>%fkg'%(m,r,t,3*3.14*(r/2)*(r/2),weight*3.71/9.807)
r=int(input('지름:'))
m=input('재질:')
t=int(input('두께:'))
result=sphere_area(r,m,t)  
print(result)  