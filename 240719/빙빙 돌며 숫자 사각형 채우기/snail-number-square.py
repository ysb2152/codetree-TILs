n,m=map(int,input().split())
L=[[0 for _ in range(n)]for _ in range(m)]
dx,dy=[0,1,0,-1],[1,0,-1,0]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m
x,y=0,0
dirc=0
L[0][0]=1
for i in range(2,n*m+1):
    nx,ny=x+dx[dirc],y+dy[dirc]
    if not in_range(nx,ny) or L[nx][ny]!=0:
        dirc=(dirc+1)%4
    x,y=x+dx[dirc],y+dy[dirc]
    L[x][y]=i
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")