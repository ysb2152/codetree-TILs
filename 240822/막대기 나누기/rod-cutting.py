import sys
n=int(input())
stick=[0]+list(map(int,input().split()))
dp=[-1]*(n+1)
dp[0]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+stick[j])
print(dp[-1])