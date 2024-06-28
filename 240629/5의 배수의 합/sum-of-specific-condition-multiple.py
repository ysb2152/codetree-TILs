a,b= map(int,input().split())
summ=0
if a<b:
    for i in range(a,b+1):
        if i%5==0:
            summ+=i
elif a>b:
    for i in range(b,a+1):
        if i%5==0:
            summ+=i
elif a==b:
    if a%5==0:
        summ+=a

print(f"{summ}")