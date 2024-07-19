n,m=map(int,input().split())
L=[[0 for _ in range(m)]for _ in range(n)]
dx,dy=[0,1,0,-1],[1,0,-1,0]
def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<m
cnt=66
dirc=0
x,y=0,0
L[0][0]='A'
for i in range(1,n*m):
    dxc,dyc=x+dx[dirc],y+dy[dirc]
    if not in_range(dxc,dyc) or L[dxc][dyc]!=0:
        dirc=(dirc+1)%4
    x,y=x+dx[dirc],y+dy[dirc]
    L[x][y]=chr(cnt+i-1)
    
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")