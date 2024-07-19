n=int(input())
dx,dy=[0, 1, -1, 0], [-1, 0, 0, 1]
L=[[0 for _ in range(1000)]for _ in range(1000)]
L[499][499]='A'
x,y=499,499
t=1
cnt=0
def in_range(x,y):
    return 0<=x and x<1000 and 0<=y and y<1000
for _ in range(n):
    dirc,leng=input().split()
    leng=int(leng)
    for i in range(0,leng):
        if dirc=='W':
            nx,ny=x+dx[0],y+dy[0]
            if  in_range(nx,ny) and L[nx][ny]=='A':
                if cnt==0:
                    print(t)
                cnt+=1
                break
            if in_range(nx,ny) and L[nx][ny]!='A':
                x,y=x+dx[0],y+dy[0]
                L[x][y]=t
                t+=1
        if dirc=='S':
            nx,ny=x+dx[1],y+dy[1]
            if in_range(nx,ny) and L[nx][ny]=='A':
                if cnt==0:
                    print(t)
                cnt+=1
                break
            if in_range(nx,ny) and L[nx][ny]!='A':
                x,y=x+dx[1],y+dy[1]
                L[x][y]=t
                t+=1
        if dirc=='N':
            nx,ny=x+dx[2],y+dy[2]
            
            if  in_range(nx,ny) and L[nx][ny]=='A':
                if cnt==0:
                    print(t)
                cnt+=1
                break
            if in_range(nx,ny) and L[nx][ny]!='A':
                x,y=x+dx[2],y+dy[2]
                
                L[x][y]=t
                t+=1
        if dirc=='E':
            nx,ny=x+dx[3],y+dy[3]
            if  in_range(nx,ny) and L[nx][ny]=='A':
                if cnt==0:
                    print(t)
                cnt+=1
                break
            if in_range(nx,ny) and L[nx][ny]!='A':
                x,y=x+dx[3],y+dy[3]
                L[x][y]=t
                t+=1
if cnt==0:
    print("-1")