n=int(input())
L=[list(map(int,input().split()))for _ in range(n)]
def in_range(a,b):
    return 0<=a<n and 0<=b<n
bomb=[]
comb=[]
max_area=-99999
for i in range(n):
    for j in range(n):
        if L[i][j]==1:
            bomb.append([i,j])
def explode(A):
    global max_area
    cnt=0
    grid=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(len(bomb)):
        if A[i]==1:
            grid[bomb[i][0]][bomb[i][1]]='B'
            for j in range(-2,3):
                new_x,new_y=bomb[i][0]+j,bomb[i][1]
                if in_range(new_x,new_y):
                    grid[new_x][new_y]='B'
        if A[i]==2:
            grid[bomb[i][0]][bomb[i][1]]='B'
            dxs,dys=[-1,1,0,0],[0,0,-1,1]
            for dx,dy in zip(dxs,dys):
                new_x,new_y=bomb[i][0]+dx,bomb[i][1]+dy
                if in_range(new_x,new_y):
                    grid[new_x][new_y]='B'
        if A[i]==3:
            grid[bomb[i][0]][bomb[i][1]]='B'
            dxs,dys=[-1,-1,1,1],[-1,1,-1,1]
            for dx,dy in zip(dxs,dys):
                new_x,new_y=bomb[i][0]+dx,bomb[i][1]+dy
                if in_range(new_x,new_y):
                    grid[new_x][new_y]='B'
    for row in grid:
        #print(row)
        for ele in row:
            
            if ele=='B':
                cnt+=1
    #print(" ")
    max_area=max(max_area,cnt)
                

def choose(num):
    if num==len(bomb)+1:
        explode(comb)
        return
    for i in range(1,4):
        comb.append(i)
        choose(num+1)
        comb.pop()
    return
    
choose(1)
print(max_area)