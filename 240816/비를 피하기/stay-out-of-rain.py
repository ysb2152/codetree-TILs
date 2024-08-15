from collections import deque

n,h,m=map(int,input().split())
visited=[[0 for _ in range(n)]for _ in range(n)]

grid=[list(map(int,input().split()))for _ in range(n)]


q=deque()

def in_range(a,b):
    return 0<=a<n and 0<=b<n
def push(a,b,s):
    visited[a][b]=1
    q.append((a,b,s))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==1:
        return False
    return True
def bfs(s):
    minimum=[]
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        a,b,s=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b):
                
                if grid[new_a][new_b]==3:
                    minimum.append(s)
                
                visited[new_a][new_b]=1
                push(new_a,new_b,s+1)
    if minimum==[]:
        return None
    else:
        return min(minimum)
                
new_grid=[[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            visited[i][j]=1
            push(i,j,1)
            new_grid[i][j]=bfs(1)
            if new_grid[i][j]==None:
                new_grid[i][j]=-1
            visited=[[0 for _ in range(n)]for _ in range(n)]
    
for row in new_grid:
    for ele in row:
        print(ele,end=" ")
    print(" ")