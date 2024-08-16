from collections import deque
q=deque()
n,k=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(n)]for _ in range(n)]
step=[[0 for _ in range(n)]for _ in range(n)]
rotten=[    (i,j) 
            for i in range(n) 
            for j in range(n)
            if grid[i][j]==2
]


def in_range(a,b):
    return 0<=a<n and 0<=b<n
def push(a,b,new_step):
    visited[a][b]=1
    step[a][b]=new_step
    q.append((a,b))
def can_move(a,b):
    return in_range(a,b) and grid[a][b]!=0 and not visited[a][b]
def bfs():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b):
                push(new_a,new_b,step[a][b]+1)
for x,y in rotten:
    push(x,y,0)
bfs()
#for row in step:
    #print(row)
for p in range(n):
    for q in range(n):
        if grid[p][q]==0:
            print("-1",end=" ")
            continue
        if grid[p][q]==1 and step[p][q]==0:
            print("-2",end=" ")
            continue
        if grid[p][q]==1:
            print(step[p][q],end=" ")
            continue
        
        if grid[p][q]==2:
            print("0",end=" ")
            continue
    print(" ")