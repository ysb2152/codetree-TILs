n,t=map(int,input().split())
order=input()
order=list(order)
dx,dy=[-1,0,1,0],[0,-1,0,1]
def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<n
L=[]

for _ in range(n):
    s=list(map(int,input().split()))
    L.append(s)
x,y=n//2,n//2
cnt=L[n//2][n//2]
dics=0
for i in range(len(order)):
    if order[i]=='L':
        dics=(dics+1)%4
    if order[i]=='R':
        dics=(dics+3)%4
    if order[i]=='F':
        dxs,dys=x+dx[dics],y+dy[dics]
        if not in_range(dxs,dys):
            continue
            
        x,y=x+dx[dics],y+dy[dics]
       
        cnt+=L[x][y]
print(cnt)