import sys
max_cnt=-sys.maxsize
n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
dp=[[0 for _ in range(n)]for _ in range(n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
cnt=1
def can_move(a,b):
    global max_cnt
    global cnt
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        new_a,new_b=a+dx,b+dy
        if in_range(new_a,new_b) and grid[new_a][new_b]>grid[a][b]:
            cnt+=1
            can_move(new_a,new_b)
            max_cnt=max(max_cnt,cnt)
            cnt=1
            
    

    
    return 0
for i in range(n):
    for j in range(n):
        can_move(i,j)
#can_move(1,1)
if max_cnt!=-sys.maxsize:
    print(max_cnt)
else:
    print("1")