import sys
n,m=map(int,input().split())
coin=[0]+list(map(int,input().split()))
dp=[-sys.maxsize]*(m+1)
dp[0]=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if i>=coin[j]:
            if dp[i-coin[j]]==-sys.maxsize:
                continue
            dp[i]=max(dp[i],dp[i-coin[j]]+1)

if dp[m]==-sys.maxsize:
    print("-1")
else:
    print(dp[m])