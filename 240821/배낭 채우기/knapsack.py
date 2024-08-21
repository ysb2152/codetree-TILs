import sys
n,m=map(int,input().split())
jewel=[tuple(map(int,input().split()))for _ in range(n)]
jewel=[0]+jewel
dp=[0]*(m+1)
dp[0]=0
for i in range(1,n+1):
    for j in range (m,-1,-1):
        if j>=jewel[i][0]:
            dp[j]=max(dp[j],dp[j-jewel[i][0]]+jewel[i][1])
print(dp[m])