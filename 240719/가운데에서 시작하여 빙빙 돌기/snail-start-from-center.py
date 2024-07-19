n=int(input())
L=[[0 for _ in range(n)]for _ in range(n)]
L[n-1][n-1]=n*n

dx,dy=[0,-1,0,1],[-1,0,1,0]
x,y=n-1,n-1
dirc=0
L[n//2][n//2]=1
cnt=n*n-1
def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<n
for _ in range(0,n*n-1):
    dxs,dys=x+dx[dirc],y+dy[dirc]
    
    if not in_range(dxs,dys) or L[dxs][dys]!=0:
        dirc=(dirc+1)%4
    x,y=x+dx[dirc],y+dy[dirc]
    
    L[x][y]=cnt
    cnt-=1
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")