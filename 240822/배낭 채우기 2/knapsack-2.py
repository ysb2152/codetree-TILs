import sys
n,m=map(int,input().split())
jewel=[tuple(map(int,input().split()))for _ in range(n)]
jewel=[0]+jewel
dp=[0]*(m+1)
dp[0]=0
for i in range(1,m+1):
    for j in range (1,n+1):
        if i>=jewel[j][0]:
            dp[i]=max(dp[i],dp[i-jewel[j][0]]+jewel[j][1])
print(dp[m])