from collections import deque
n,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
start=[tuple(map(int,input().split()))for _ in range(k)]
order=1
q=deque()
max_cnt=-99999
def in_range(a,b):
    return 0<=a<n and 0<=b<n
visited=[[0 for _ in range(n)]for _ in range(n)]
def push(a,b):
    global order
    grid[a][b]=order
    order+=1
    visited[a][b]=1
    q.append((a,b))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==1:
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
for i in range(k):
    a,b=start[i]
    a,b=a-1,b-1
    if visited[a][b]:
        continue
    push(a,b)
    bfs()
    #for row in grid:
        #print(row)
for p in range(n):
    for s in range(n):
        max_cnt=max(max_cnt,grid[p][s])
print(max_cnt)