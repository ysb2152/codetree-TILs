n=int(input())
summ=0
cnt=0
for i in range(1,n+1):
    i=int(input())
    summ+=i
    cnt+=1
print(f"{summ}",end=" ")
print(f"{(summ/cnt):.1f}")