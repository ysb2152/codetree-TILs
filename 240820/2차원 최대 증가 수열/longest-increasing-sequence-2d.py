import sys
n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
dp=[[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j]=-sys.maxsize
dp[0][0]=1
for i in range(n):
    for j in range(m):
        for p in range(i):
            for q in range(j):
                if dp[p][q]==-sys.maxsize:
                    continue
                if grid[p][q]<grid[i][j]:
                    dp[i][j]=max(dp[i][j],dp[p][q]+1)
ans=-sys.maxsize
for row in dp:
    for ele in row:
        ans=max(ans,ele)
print(ans)