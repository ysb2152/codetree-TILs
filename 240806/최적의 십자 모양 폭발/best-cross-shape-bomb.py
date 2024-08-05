n=int(input())
L=[list(map(int,input().split()))for _ in range(n)]
r,c=2,1
dxs,dys=[1,0,-1,0],[0,1,0,-1]
max_cnt=-99999
def in_range(a,b):
    return 0<=a<n and 0<=b<n
def exp(r,c):
    comp=[L[:] for L in L]
    bomb=comp[r][c]
    
    comp[r][c]=0
    
    for dx,dy in zip(dxs,dys):
        for i in range(1,bomb):
            if in_range(r+i*dx,c+i*dy):
                comp[r+i*dx][c+i*dy]=0
    return comp

def count(A):
    global max_cnt
    cnt=0
    for i in range(n):
        for j in range(n):
            for dx, dy in zip(dxs,dys):
                if A[i][j]!=0 and in_range(i+dx,j+dy) and A[i][j]==A[i+dx][j+dy]:
                    cnt+=1
                    
        max_cnt=max(max_cnt,cnt)
    return cnt

for i in range(n):
    for j in range(n):
        ans2=[[0 for _ in range(n)]for _ in range(n)]
        cal=exp(i,j)
        
        for k in range(n):
            ans2_row=n-1
            for l in range(n-1,-1,-1):
                if cal[l][k]!=0:
                    ans2[ans2_row][k]=cal[l][k]
            
                    ans2_row-=1
        count(ans2)
print(max_cnt//2)