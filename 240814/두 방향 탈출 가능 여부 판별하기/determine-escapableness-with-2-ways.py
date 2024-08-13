n,m=map(int,input().split())
visited=[[0 for _ in range(m)]for _ in range(n)]
grid=[list(map(int,input().split())) for _ in range(n)]
order=0
def in_range(a,b):
    return 0<=a<n and 0<=b<m
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==0:
        return False
    return True
def dfs(a,b):
    global order
    dxs,dys=[1,0],[0,1]
    for dx,dy in zip(dxs,dys):
        new_a,new_b=a+dx,b+dy
        if can_move(new_a,new_b):
            order+=1
            visited[new_a][new_b]=1
            grid[new_a][new_b]=order
            dfs(new_a,new_b)
grid[0][0]=1
order+=1
visited[0][0]=1
dfs(0,0)
if grid[n-1][m-1]>1:
    print("1")
else:
    print("0")