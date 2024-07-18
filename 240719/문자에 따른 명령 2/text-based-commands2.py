a=input()
a=list(a)
x,y=0,0
dx,dy=[0,1,0,-1],[1,0,-1,0]
dir_num=0
for ele in a:
    if ele=='L':
        dir_num=(dir_num+3)%4
        
    if ele=='R':
        dir_num=(dir_num+1)%4
        
    if ele=='F':
        x,y=dx[dir_num]+x,y+dy[dir_num]
print(x,y)