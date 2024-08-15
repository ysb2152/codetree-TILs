from collections import deque
q=deque()
n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(m)]for _ in range(n)]
step=[[0 for _ in range(m)]for _ in range(n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<m
def push(a,b,s):
    step[a][b]=s
    visited[a][b]=1
    q.append((a,b))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==0:
        return False
    return True
def bfs():
    while q:
        a,b=q.popleft()
        dxs,dys=[-1,1,0,0],[0,0,-1,1]
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b):
                visited[new_a][new_b]=1
                push(new_a,new_b,step[a][b]+1)
push(0,0,0)
bfs()
if step[-1][-1]>=2:
    print(step[-1][-1])
else:
    print("-1")