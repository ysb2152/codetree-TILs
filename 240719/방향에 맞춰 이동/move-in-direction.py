n=int(input())
x=0
y=0
dx,dy=[1,0,-1,0],[0,-1,0,1]
for _ in range(n):
    direction,leng=input().split()
    leng=int(leng)
    if direction=='E':
        dir_num=0
    if direction=='S':
        dir_num=1
    if direction=='W':
        dir_num=2
    if direction=='N':
        dir_num=3
    x,y=x+dx[dir_num]*leng,y+dy[dir_num]*leng
    
    
print(x,y)