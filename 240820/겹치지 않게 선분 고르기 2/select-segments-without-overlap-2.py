n=int(input())
line=[tuple(map(int,input().split()))for _ in range(n)]
line.sort()
dp=[1]*n
for i in range(1,n):
    x,y=line[i]
    for j in range(i):
        beforex,beforey=line[j]
        if (beforex<x and beforey<x) or (beforex>y and beforey>y):
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))