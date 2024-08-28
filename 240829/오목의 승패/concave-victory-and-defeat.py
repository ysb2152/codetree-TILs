import sys
grid=[list(map(int,input().split()))for _ in range(19)]
dxs,dys=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]
def in_range(a,b):
    return 0<=a<19 and 0<=b<19
cnt=[[]for _ in range(8)]
def check(a,b,direction):
    dx,dy=dxs[direction],dys[direction]
    
    new_a,new_b=a+dx,b+dy
    if in_range(new_a,new_b) and grid[new_a][new_b]==grid[a][b]:
        check(new_a,new_b,direction)
        cnt[direction].append((new_a,new_b,direction))

for j in range(19):
    for k in range(19):
        if grid[j][k]!=0:
            for i in range(8):
                cnt[i].append((j,k,i))
                check(j,k,i)
                if len(cnt[i])==5:
                    a=cnt[i][0]
                    p,q,r=cnt[i][0]
                    print(grid[p][q])
                    print(p+1,q+1)
                    sys.exit()
                #print(cnt)
                cnt=[[]for _ in range(8)]