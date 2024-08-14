from collections import deque
q=deque()
n,k=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
r,c=tuple(map(int,input().split()))
visited=[[0 for _ in range(n)]for _ in range(n)]
r,c=r-1,c-1
cnt=1
dxs,dys=[-1,0,0,1],[0,-1,1,0]
possible=[]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def push(a,b):
    global cnt
    visited[a][b]=1
    cnt+=1
    q.append((a,b))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]>=grid[r][c]:
        return False
    return True
def bfs():
    global possible
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
                new_a,new_b=a+dx,b+dy
                if can_move(new_a,new_b):
                    visited[new_a][new_b]=1
                    possible.append([new_a,new_b,grid[new_a][new_b]])
                    push(new_a,new_b)
                
for _ in range(k):
                   
    push(r,c)
    bfs()
    possible.sort(key=lambda x:(-x[2],x[0],x[1]))
    r,c=possible[0][0],possible[0][1]
    #print(r,c)
    #print(possible)
    #print(" ")
    possible=[]
    visited=[[0 for _ in range(n)]for _ in range(n)]
print(r+1,c+1)