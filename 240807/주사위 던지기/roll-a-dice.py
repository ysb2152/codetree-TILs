n,m,r,c=map(int,input().split())
order=list(input().split())
r,c=r-1,c-1
def in_range(a,b):
    return 0<=a<n and 0<=b<n
grid=[[0 for _ in range(n)]for _ in range(n)]
dxs,dys=[0,0,-1,1],[-1,1,0,0]
dice=[
    [0,5,0],
    [4,6,3],
    [0,2,0]
]
def curr():
    return dice[1][1]
def roll(direction):
    if direction=='L':
        dice[1]=[7-curr(),dice[1][0],dice[1][1]]
        
    if direction=='R':
        dice[1]=[dice[1][1],dice[1][2],7-curr()]
        
    if direction=='U':
        dice[0][1],dice[1][1],dice[2][1]=7-curr(),dice[0][1],dice[1][1]
        
    if direction=='D':
        dice[0][1],dice[1][1],dice[2][1]=dice[1][1],dice[2][1],7-curr()
       
        
grid[r][c]=curr()
for i in range(m):
    if order[i]=='L':
        r1,c1=r+dxs[0],c+dys[0]
        if not in_range(r1,c1):
            continue
        r,c=r1,c1
        roll(order[i])
        grid[r][c]=curr()
    if order[i]=='R':
        r1,c1=r+dxs[1],c+dys[1]
        if not in_range(r1,c1):
            continue
        r,c=r1,c1
        roll(order[i])

        grid[r][c]=curr()
    if order[i]=='U':
        r1,c1=r+dxs[2],c+dys[2]
        if not in_range(r1,c1):
            continue
        r,c=r1,c1
        roll(order[i])
        
        grid[r][c]=curr()
    if order[i]=='D':
        r1,c1=r+dxs[3],c+dys[3]
        if not in_range(r1,c1):
            continue
        r,c=r1,c1
        roll(order[i])
        grid[r][c]=curr()
   
cnt=0
for row in grid:
    
    for ele in row:
        cnt+=ele
print(cnt)