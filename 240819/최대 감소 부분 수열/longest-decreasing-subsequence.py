n=int(input())
L=[0]+list(map(int,input().split()))
dp=[0 for _ in range(n+1)]
dp[1]=1
for i in range(1,n+1):
    for j in range(i):
        if L[j]>L[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))