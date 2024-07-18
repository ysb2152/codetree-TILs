n=int(input())
L=[]
p=[[0 for _  in range(n)]for _ in range(n)]
for _ in range(n):
    a=list(map(int,input().split()))
    L.append(a)
cnt=0


dxs,dys=[0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
for i in range(n):
    for j in range(n):
        for dx,dy in zip(dxs,dys):
            x,y=i+dx,j+dy
            
            if in_range(x,y) and L[x][y]==1:
                p[i][j]+=1
            x,y=0,0
for row in p:
    for ele in row:
        if ele>=3:
            cnt+=1
print(cnt)