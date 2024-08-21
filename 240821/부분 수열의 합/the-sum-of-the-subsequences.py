import sys
n,m=map(int,input().split())
A1=list(map(int,input().split()))
A=[0]+A1
dp=[0]*(m+1)
for i in range(m+1):
    dp[i]=sys.maxsize
dp[0]=0



for i in range(1,n+1):
    for j in range(m,-1,-1):
        if j>=A[i]:
            dp[j]=min(dp[j],dp[j-A[i]]+1)
if dp[m]==sys.maxsize:
    print("No")
else:
    print("Yes")