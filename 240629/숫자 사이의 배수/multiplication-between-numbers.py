a,b=map(int,input().split())
summ=0
cnt=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        summ+=i
        cnt+=1
print(f"{summ}",end=" ")
print(f"{(summ/cnt):.1f}")