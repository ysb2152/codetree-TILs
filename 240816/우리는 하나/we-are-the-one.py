import sys
from collections import deque
q=deque()
n,k,u,d=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(n)]for _ in range(n)]
choosed_city=[]
city_visited=[[0 for _ in range(n)]for _ in range(n)]
max_cnt=-sys.maxsize
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def can_move(a,b,new_a,new_b):
    if not in_range(new_a,new_b):
        return False
    if visited[new_a][new_b] or abs(grid[a][b]-grid[new_a][new_b])<u or abs(grid[a][b]-grid[new_a][new_b])>d:
        return False
    return True
def push(a,b):
    visited[a][b]=1
    q.append((a,b))
def bfs():
    while q:
        
        a,b=q.popleft()
        #print(a,b)
        dxs,dys=[-1,1,0,0],[0,0,-1,1]
        for dx,dy in zip(dxs,dys):
            new_a,new_b=a+dx,b+dy
            if can_move(a,b,new_a,new_b):
                #print(new_a,new_b)
                visited[new_a][new_b]=1
                push(new_a,new_b)
def choose(num):
    global max_cnt
    global city_visited
    global visited  
    if num==k+1:
        city_visited=[[0 for _ in range(n)]for _ in range(n)]
        cnt=0
        for j in range(len(choosed_city)):
            #print(choosed_city)
            starta,startb=choosed_city[j]
            if visited[starta][startb]==1:
                continue
            push(starta,startb)
            visited[starta][startb]=1
            bfs()
        #print(visited)
        for row in visited:
            
            cnt+=row.count(1)
        max_cnt=max(max_cnt,cnt)
        visited=[[0 for _ in range(n)]for _ in range(n)]
        city_visited=[[0 for _ in range(n)]for _ in range(n)]
        return
    for i in range(n):
        for j in range(n):
            if city_visited[i][j]:
                continue
            if (i,j) in choosed_city:
                continue
            choosed_city.append((i,j))
            city_visited[i][j]=1
            choose(num+1)
            choosed_city.pop()
    return
choose(1)
print(max_cnt)