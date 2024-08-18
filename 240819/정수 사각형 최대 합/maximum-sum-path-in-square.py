n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=grid[0][0]
for i in range(1,n):
    dp[i][0]=dp[i-1][0]+grid[i][0]
for i in range(1,n):
    dp[0][i]=dp[0][i-1]+grid[0][i]

for j in range(1,n):
    for k in range(1,n):
        dp[j][k]=max(dp[j-1][k]+grid[j][k],dp[j-1][k-1]+grid[j][k],dp[j][k-1]+grid[j][k])



print(dp[n-1][n-1])