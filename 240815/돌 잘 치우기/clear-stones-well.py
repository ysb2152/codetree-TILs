import sys
from collections import deque
n,k,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
start_point=[tuple(map(int,input().split())) for _ in range(k)]
visited=[[0 for _ in range(n)]for _ in range(n)]
max_cnt=-sys.maxsize
for a in range(k):
    startpointx,startpointy=start_point[a]
    start_point[a]=(startpointx-1,startpointy-1)
dxs,dys=[-1,1,0,0],[0,0,-1,1]
remove_rocks=[]
to_remove_rocks=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            to_remove_rocks.append((i,j))
q=deque()
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def push(a,b):
    visited[a][b]=1
    q.append((a,b))
def can_move(a,b,grid):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==1:
        return False
    return True
def bfs(new_grid):
    global visited
      
    #for row in new_grid:
        #print(row)
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b,new_grid):
                visited[new_a][new_b]=1
                
                push(new_a,new_b)
    #for row in new_grid:
        #print(row)
    
def choose_remove_rocks(num,grid):
    new_grid=[grid[:]for grid in grid]
        
    global max_cnt
    global visited
    if m==0:
        for j in range(k):
            r,c=start_point[j]
            if visited[r][c]==1:
                continue
            push(r,c)
            bfs(new_grid)
        ones=0
        for row in visited:
            ones+=row.count(1)
        
        max_cnt=max(max_cnt,ones)
            
        return
    if num==m+1:
        #print(remove_rocks)
        for i in range(len(remove_rocks)):
            a,b=remove_rocks[i]
            new_grid[a][b]=0
        #for row in new_grid:
            #print(row)
        #print(" ")
        for j in range(k):
            r,c=start_point[j]
            push(r,c)
            bfs(new_grid)
        ones=0
        
        for row in visited:
            ones+=row.count(1)
        max_cnt=max(max_cnt,ones)
        
        visited=[[0 for _ in range(n)]for _ in range(n)]
            
        
        return
    for i in range(len(to_remove_rocks)):
        if to_remove_rocks[i] in remove_rocks:
            continue
        remove_rocks.append(to_remove_rocks[i])
        choose_remove_rocks(num+1,grid)
        remove_rocks.pop()
    return

  
choose_remove_rocks(1,grid)        
print(max_cnt)