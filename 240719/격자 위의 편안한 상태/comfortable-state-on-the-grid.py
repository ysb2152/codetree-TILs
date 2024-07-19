n,m=map(int,input().split())
L=[[0 for _ in range(n)]for _ in range(n)]
dxs,dys=[0,1,0,-1],[1,0,-1,0] 

def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<n
for _ in range(m):
    r,c=map(int,input().split())
    r-=1
    c-=1
    L[r][c]=1
    cnt=0
    for dx,dy in zip(dxs,dys):
        r1,c1=r+dx,c+dy
        if in_range(r1,c1) and L[r1][c1]==1:
            cnt+=1
    if cnt==3:
        
        print("1")
        cnt=0
    else:
        print("0")
        cnt=0