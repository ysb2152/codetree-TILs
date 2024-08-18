import sys
max_cnt=-sys.maxsize
n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
dp=[[0 for _ in range(n)]for _ in range(n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<n

def can_move(a,b):
    if dp[a][b]!=0:
        return dp[a][b]
    cnt=1
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        new_a,new_b=a+dx,b+dy
        if in_range(new_a,new_b) and grid[new_a][new_b]>grid[a][b]:
            cnt=max(cnt,can_move(new_a,new_b)+1)
    dp[a][b]=cnt
    return cnt
            
    

    
    return 0
for i in range(n):
    for j in range(n):
        max_cnt=max(max_cnt,can_move(i,j))
#can_move(1,1)
if max_cnt!=-sys.maxsize:
    print(max_cnt)
else:
    print("1")