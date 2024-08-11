n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
dir_grid=[list(map(int,input().split()))for _ in range(n)]
r,c=map(int,input().split())
r,c=r-1,c-1
dxs,dys=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
max_cnt=-99999
for i in range(n):
    for j in range(n):
        dir_grid[i][j]=dir_grid[i][j]-1

ans=[]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def can_move(a,b):
    for i in range(n):
        
        if in_range(r+dxs[dir_grid[a][b]]*i,b+dys[dir_grid[a][b]]*i) and grid[r+dxs[dir_grid[a][b]]*i][b+dys[dir_grid[a][b]]*i]>grid[a][b]:
            return True
    return False

def choose(r,c):
    global ans,max_cnt
    beforeans=ans
    if can_move(r,c)==False:
        #print(ans)
        max_cnt=max(max_cnt,len(ans))
        ans=beforeans
        
        
    for i in range(1,n+1):
        new_r,new_c=r+dxs[dir_grid[r][c]]*i,c+dys[dir_grid[r][c]]*i
        
        if in_range(new_r,new_c) and grid[new_r][new_c]>grid[r][c]:
            
            ans.append(grid[new_r][new_c])
            choose(new_r,new_c)
            #print(ans)
            ans.pop()
        
        
        #choose(r,c)
            
        
    
choose(r,c)
print(max_cnt)