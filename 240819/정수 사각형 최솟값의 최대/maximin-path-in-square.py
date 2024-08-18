n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
dp=[[0 for  _ in range(n)]for _ in range(n)]
dp[0][0]=grid[0][0]
for i in range(1,n):
    dp[0][i]=min(dp[0][i-1],grid[0][i])
   
for i in range(1,n):
    dp[i][0]=min(dp[i-1][0],grid[i][0])
for i in range(1,n):
    for j in range(1,n):
        if i==n-1 and j==n-1:
            break
        dp[i][j]=min(dp[i-1][j],dp[i][j-1])
if max(dp[n-2][n-1],dp[n-1][n-2])<=grid[n-1][n-1]:
    print(max(dp[n-2][n-1],dp[n-1][n-2]))
else:
    print(grid[n-1][n-1])