n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(n)]for _ in range(n)]
town=1
people=0
towns=[0 for _ in range(n*n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def can_move(a,b):
    if not in_range(a,b):
        return False
    if visited[a][b] or grid[a][b]==0:
        return False
    return True
def dfs(a,b):
    global town
    global people
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        new_a,new_b=a+dx,b+dy
        if can_move(new_a,new_b):
            visited[new_a][new_b]=1
            grid[new_a][new_b]=town
            people+=1
            dfs(new_a,new_b)
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            town+=1
            people+=1
            grid[i][j]=town
            visited[i][j]=1
            dfs(i,j)
            towns[town]=people
            people=0


towns.sort()
cnt=0
for i in range(len(towns)):
    if towns[i]!=0:
        cnt+=1
print(cnt)
for i in range(len(towns)):
    if towns[i]!=0:
        print(towns[i])