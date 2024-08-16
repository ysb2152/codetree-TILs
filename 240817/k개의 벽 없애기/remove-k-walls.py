from collections import deque
q=deque()
n,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
new_grid=[grid[:]for grid in grid]
visited=[[0 for _ in range(n)]for _ in range(n)]
step=[[0 for _ in range(n)]for _ in range(n)]
choosed_walls=[]
walls=[]
r2c2s=[]
min_second=99999
r1,c1=map(int,input().split())
r1,c1=r1-1,c1-1
r2,c2=map(int,input().split())
r2,c2=r2-1,c2-1
dxs,dys=[-1,1,0,0],[0,0,-1,1]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            walls.append((i,j))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or new_grid[a][b]==1:
        return False
    return True
def push(a,b,s):
    visited[a][b]=1
    step[a][b]=s
    q.append((a,b))
def bfs():
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b):
                
                push(new_a,new_b,step[a][b]+1)
    
    
def choose(num,cnt):
    global new_grid
    global visited
    global step
    if num==k+1:
        #print(choosed_walls)
        new_grid=[grid[:]for grid in grid]
        visited=[[0 for _ in range(n)]for _ in range(n)]
        step=[[0 for _ in range(n)]for _ in range(n)]
        for p,q in choosed_walls:
            new_grid[p][q]=0
        #for row in new_grid:
            #print(row)
        #print(" ")
        push(r1,c1,0)
        bfs()
        #for row in step:
            #print(row)
        #print(" ")
        r2c2s.append((step[r2][c2]))
        return
        
    for i in range(cnt,len(walls)):
        choosed_walls.append(walls[i])
        choose(num+1,cnt+1)
        choosed_walls.pop()
    return
choose(1,0)
for ele in r2c2s:
    if ele!=0:
        min_second=min(min_second,ele)
if min_second==99999:
    print("-1")
else:
    print(min_second)