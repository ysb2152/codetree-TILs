n,m=map(int,input().split())
grid=[[0 for _ in range(n)]for _ in range(n)]
for _ in range(m):
    a,b=tuple(map(int,input().split()))
    grid[a-1][b-1]=1
    grid[b-1][a-1]=1
visited=[False]*n
cnt=0
def dfs(vertex):
    global cnt
    for curr_v in range(0,n):
        if grid[vertex][curr_v] and not visited[curr_v]:
            cnt+=1
            visited[curr_v]=True
            dfs(curr_v)
visited[0]=True
dfs(0)
print(cnt)