n,m=map(int,input().split())
L=list(map(int,input().split()))
max_sum=0
for i in range(n):
    summ=0
    cnt=1
    a=L[i]
    for j in range(m):
        summ+=a
        
        a-=1
        a=L[a]
    max_sum=max(max_sum,summ)
        
    
print(max_sum)