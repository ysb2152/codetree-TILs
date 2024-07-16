a,b,c,d=map(int,input().split())
time=0
while True:
    if a==c and b==d:
        break
    b+=1
    time+=1
    if b==60:
        a+=1
        b=0
print(time)