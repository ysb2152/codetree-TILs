n=int(input())
L=[list(map(int,input().split()))for _ in range(n)]
r,c=map(int,input().split())
r,c=r-1,c-1
dxs,dys=[1,0,-1,0],[0,1,0,-1]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def exp(r,c):
    bomb=L[r][c]
    
    L[r][c]=0
    
    for dx,dy in zip(dxs,dys):
        for i in range(1,bomb):
            if in_range(r+i*dx,c+i*dy):
                L[r+i*dx][c+i*dy]=0

ans2=[[0 for _ in range(n)]for _ in range(n)]

exp(r,c)


for i in range(n):
    ans2_row=n-1
    for j in range(n-1,-1,-1):
        if L[j][i]!=0:
            ans2[ans2_row][i]=L[j][i]
            
            ans2_row-=1


for row in ans2:
    for ele in row:
        print(ele,end=" ")
    print(" ")