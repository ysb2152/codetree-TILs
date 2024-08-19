import sys
n=int(input())
L=list(map(int,input().split()))
dp=[0 for _ in range(n)]
for i in range(n):
    dp[i]=-sys.maxsize
dp[0]=0
for i in range(1,n):
    for j in range(0,i):
        if dp[j]==-sys.maxsize:
            continue
        if j+L[j]>=i:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))