m1,d1,m2,d2=map(int,input().split())
days=["0","Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
monthdays=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dd=0
if m1<m2 or (m1==m2 and d1<d2):
    while True:
        if m1==m2 and d1==d2:
            break
        dd+=1
        d1+=1
        if d1>monthdays[m1]:
            m1+=1
            d1=1
else:
    while True:
        if m1==m2 and d1==d2:
            break
        dd+=1
        d2+=1
        if d2>monthdays[m2]:
            m2+=1
            d2=1
print(days[dd%7])