m1,d1,m2,d2=map(int,input().split())
days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer=0
while True:
    if m1==m2 and d1==d2:
        break
    answer+=1
    d1+=1
    if d1>days[m1]:
        m1+=1
        d1=1
print(answer+1)