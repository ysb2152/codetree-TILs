n=int(input())
info=[tuple(map(int,input().split()))for _ in range(n)]
min_x=9999
for i in range(1,11):
    k=i
    for j in range(n):
        a,b=info[j]
        
        if j==0:
            k*=2
        
        if a<=k and k<=b:
            
            k*=2
            
        else:
            break
        if j==n-1:
            min_x=min(min_x,i)
print(min_x)