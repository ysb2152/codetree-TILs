n=int(input())
line=[tuple(map(int,input().split()))for _ in range(n)]
line.sort()
dp=[0]*n
for i in range(n):
    dp[i]=line[i][2]
for i in range(1,n):
    x,y,m=line[i]
    for j in range(i):
        beforex,beforey,beforem=line[j]
        if (beforex<x and beforey<x) or (beforex>y and beforey>y):
            dp[i]=max(dp[i],dp[j]+m)
print(max(dp))