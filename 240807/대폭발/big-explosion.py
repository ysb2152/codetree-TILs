n,m,r,c=map(int,input().split())
r,c=r-1,c-1
grid=[[0 for _ in range(n)]for _ in range(n)]
grid[r][c]=1
def in_range(a,b):
    return 0<=a<n and 0<=b<n
dxs,dys=[-1,1,0,0],[0,0,-1,1]

cnt=1
bomb=[(r,c)]

for cnt in range(1,m+1):
    dist=2**(cnt-1)
    new=[]
    for a,b in bomb:
        for dx,dy in zip(dxs,dys):
            new_r=a+dx*dist
            new_c=b+dy*dist
        
            if in_range(new_r,new_c) and (new_r,new_c) not in bomb:
                new.append((new_r,new_c))
    for i in range(len(new)):
        bomb.append(new[i])

print(len(bomb))