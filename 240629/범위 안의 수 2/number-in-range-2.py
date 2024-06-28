summ=0
cnt=0
for _ in range(10):
    i=int(input())
    if 0<=i<=200:
        summ+=i
        cnt+=1
print(f"{summ}",end=" ")
print(f"{(summ/cnt):.1f}")