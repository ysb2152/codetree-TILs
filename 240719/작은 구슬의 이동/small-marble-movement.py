n,t=map(int,input().split())
r,c,d=input().split()
r,c=int(r),int(c)

def in_range(a,b):
    return 0<a and a<=n and 0<b and b<=n
dx,dy=[0,1,-1,0],[1,0,0,-1]
cnt=0
D={'R':0,'D':1,'U':2,'L':3}
for i in range(1,t+1):
    if d=='R':
        r,c=r+dx[D[d]],c+dy[D[d]]
        if in_range(r,c)==False:
            
            r,c=r-dx[D[d]],c-dy[D[d]]
            d='L'
            continue
            
            
    if d=='D':
        r,c=r+dx[D[d]],c+dy[D[d]]
        if in_range(r,c)==False:
            r,c=r-dx[D[d]],c-dy[D[d]]
            d='U'
            continue
            
    if d=='U':
        r,c=r+dx[D[d]],c+dy[D[d]]
        if in_range(r,c)==False:
            r,c=r-dx[D[d]],c-dy[D[d]]
            d='D'
            continue
            
    if d=='L':
        r,c=r+dx[D[d]],c+dy[D[d]]
        
        if in_range(r,c)==False:
            
            r,c=r-dx[D[d]],c-dy[D[d]]
            d='R'
            continue
    
  
print(r,c)