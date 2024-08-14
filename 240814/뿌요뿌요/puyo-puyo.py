import sys
n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(n)]for _ in range(n)]
cnt=1

explode=0
max_blocks=-sys.maxsize
dxs,dys=[-1,1,0,0],[0,0,-1,1]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b]:
        return False
    return True
def dfs(a,b):
    global cnt,max_blocks,explode
    for dx,dy in zip(dxs,dys):
        new_a,new_b=a+dx,b+dy
        if can_move(new_a,new_b) and grid[a][b]==grid[new_a][new_b]:
            cnt+=1
            visited[new_a][new_b]=1
            if cnt==4:
                explode+=1
            max_blocks=max(max_blocks,cnt)
            dfs(new_a,new_b)
for i in range(n):
    for j in range(n):
        visited[i][j]=1
        dfs(i,j)
        cnt=1
print(explode,max_blocks)