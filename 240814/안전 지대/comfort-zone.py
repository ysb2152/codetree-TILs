n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(m)]for _ in range(n)]
keys=[0 for _ in range(105)]
beforegrid=[grid[:]for grid in grid]
beforevisited=[visited[:]for visited in visited]
cnt=65
dxs,dys=[-1,1,0,0],[0,0,-1,1]
def in_range(a,b):
    return 0<=a<n and 0<=b<m
def can_move(a,b,k):
    if not in_range(a,b):
        return False
    if grid[a][b]==chr(cnt):
        return False
    if visited[a][b] or grid[a][b]<=k:
        return False
    return True
def dfs(a,b,k):
    
    for dx,dy in zip(dxs,dys):
        new_a,new_b=a+dx,b+dy
        if can_move(new_a,new_b,k):
            visited[new_a][new_b]=1
            grid[new_a][new_b]=chr(cnt)
            
            dfs(new_a,new_b,k)
def find_areas(k):
    combs=[]
    for i in range(n):
        for j in range(m):
            if isinstance(grid[i][j],str):
                if grid[i][j] not in combs:
                    combs.append(grid[i][j])
    keys[k]=len(combs)

for k in range(1,101):
    for i in range(n):
        for j in range(m):
            if can_move(i,j,k):
            
                visited[i][j]=1
                grid[i][j]=chr(cnt)
                dfs(i,j,k)
                cnt+=1
    find_areas(k)
    #for row in grid:
        #print(row)
    #print(" ")
    grid=[beforegrid[:] for beforegrid in beforegrid]
    visited=[[0 for _ in range(m)]for _ in range(n)]
    cnt=65
print(keys.index(max(keys)),end=" ")
print(max(keys))