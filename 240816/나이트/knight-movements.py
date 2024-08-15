from collections import deque
q=deque()
n=int(input())
r1,c1,r2,c2=map(int,input().split())
r1,c1,r2,c2=r1-1,c1-1,r2-1,c2-1
grid=[[0 for _ in range(n)]for _ in range(n)]
visited=[[0 for _ in range(n)]for _ in range(n)]
step=[[0 for _ in range(n)]for _ in range(n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def push(a,b,s):
    step[a][b]=s
    visited[a][b]=1
    q.append((a,b))
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b]:
        return False
    return True
def bfs():
    while q:
        a,b=q.popleft()
        dxs,dys=[-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,2,1,-1,-2]
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(new_a,new_b):
                visited[new_a][new_b]=1
                push(new_a,new_b,step[a][b]+1)
push(r1,c1,0)
bfs()
if step[r2][c2]!=0:
    print(step[r2][c2])
else:
    print("-1")