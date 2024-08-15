from collections import deque
q=deque()
n,h,m=map(int,input().split())
visited=[[0 for _ in range(n)]for _ in range(n)]
step=[[0 for _ in range(n)]for _ in range(n)]
grid=[list(map(int,input().split()))for _ in range(n)]
safearea=[]
people=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            people.append((i,j))
        if grid[i][j]==3:
            safearea.append((i,j))
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def push(a,b,s):
    visited[a][b]=1
    step[a][b]=s
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
                visited[new_a][new_b]
                push(new_a,new_b,step[a][b]+1)
new_grid=[[0 for _ in range(n)]for _ in range(n)]

for k in range(h):
    a,b=people[k]
    visited[a][b]=1
    push(a,b,0)
    bfs()
    min_move=99999999
    for p in range(len(safearea)):
        x1,y1=safearea[p]
        if step[x1][y1]!=0:
            min_move=min(min_move,step[x1][y1])
    new_grid[a][b]=min_move
    if (a,b) in people and new_grid[a][b]==min_move:
        new_grid[a][b]=-1
    visited=[[0 for _ in range(n)]for _ in range(n)]
    step=[[0 for _ in range(n)]for _ in range(n)]


    
for row in new_grid:
    for ele in row:
        print(ele,end=" ")
    print(" ")