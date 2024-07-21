n=int(input())
L=[tuple(map(int,input().split()))for _ in range(n)]

max_time=-999
for i in range(n):
    cnt=0
    time=[0 for _ in range(20000)]
    for j in range(n):
        if j==i:
            continue
        start,end=L[j]
        
        for k in range(start,end):
            time[k]=1
        
    for ele in time:
        if ele==1:
            cnt+=1
    
    max_time=max(max_time,cnt)
    
print(max_time)