n,r,c=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(n)]
dxs,dys=[-1,1,0,0],[0,0,-1,1]
r,c=r-1,c-1
def in_range(a,b):
    return 0<=a<n and 0<=b<n
max_num=L[r][c]
print(max_num,end=" ")
while True:
    beforer=r
    beforec=c
    for dx,dy in zip(dxs,dys):
        a,b=r+dx,c+dy
        if in_range(a,b) and L[a][b]>max_num:
            max_num=L[a][b]
            print(max_num,end=" ")
            r,c=a,b
    if beforer==r and beforec==c:
        break