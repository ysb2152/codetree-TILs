order=input()
order=list(order)
L=[[0 for _ in range(1000)]for _ in range(1000)]
dxs,dys=[-1,0,1,0],[0,1,0,-1]
a,b=dxs[0],dys[0]
x,y=500,500
L[x][y]='A'
dir_num=0
def in_range(a,b):
    return 0<=a and a<1000 and 0<=b and b<1000

for i in range(len(order)):
    
    if order[i]=='L':
        dir_num=(dir_num+3)%4
        
    if order[i]=='R':
        
        dir_num=(dir_num+1)%4
        
    if order[i]=='F':
        a,b=x+dxs[dir_num],y+dys[dir_num]
        if in_range(a,b):
            x,y=x+dxs[dir_num],y+dys[dir_num]
            if L[x][y]=='A':
                print(i+1)
            L[x][y]=i+1