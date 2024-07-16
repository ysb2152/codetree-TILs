m1,d1,m2,d2=map(int,input().split())
A=input()
days=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
L=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
L1=[0 for _ in range(7)]
day=0
while True:
    if m1==m2 and d1==d2:
        break
    day+=1
    d1+=1
    if d1>days[m1]:
        m1+=1
        d1=1
for i in range(1,day+1):
    L1[i%7]+=1
print(L1[L.index(A)])