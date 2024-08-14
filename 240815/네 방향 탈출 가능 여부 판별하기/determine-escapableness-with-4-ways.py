from collections import deque
n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(m)]for _ in range(n)]

order=1
def in_range(a,b):
    return 0<=a<n and 0<=b<m
q=deque()
def push(a,b):
    global order
    grid[a][b]=order
    order+=1
    visited[a][b]=1
    q.append((a,b))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==0:
        return False
    return True
def bfs():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b):
                push(new_a,new_b)
push(0,0)
bfs()
if grid[n-1][m-1]>1:
    print("1")
else:
    print("0")