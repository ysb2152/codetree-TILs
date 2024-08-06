n,m,r,c=map(int,input().split())
r,c=r-1,c-1
grid=[[0 for _ in range(n)]for _ in range(n)]
grid[r][c]=1
def in_range(a,b):
    return 0<=a<n and 0<=b<n
dxs,dys=[-1,1,0,0],[0,0,-1,1]
cnt=1
r1=r
c1=c
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            for dx,dy in zip(dxs,dys):
                new_r=r1+dx*cnt
                new_c=c1+dy*cnt
                if in_range(new_r,new_c):
                    r,c=r1+dx,c1+dy
                    grid[r][c]=1
cnt+=1




for row in grid:
    print(row)