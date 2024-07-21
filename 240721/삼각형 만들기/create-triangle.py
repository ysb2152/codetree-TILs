import sys
n=int(input())
L=[tuple(map(int,input().split())) for _ in range(n)]

def tri(a,b,c):
    p1x,p1y=L[a]
    p2x,p2y=L[b]
    p3x,p3y=L[c]
    if  p1x==p2x:
        if p2y==p3y:
            return (p1x*p2y+p2x*p3y+p3x*p1y)-(p2x*p1y+p3x*p2y+p1x*p3y)
        if p1y==p3y:
            return (p1x*p2y+p2x*p3y+p3x*p1y)-(p2x*p1y+p3x*p2y+p1x*p3y)
        else:
            return 0
    if  p1x==p3x:
        if p1y==p2y:
            return (p1x*p2y+p2x*p3y+p3x*p1y)-(p2x*p1y+p3x*p2y+p1x*p3y)
        if p2y==p3y:
            return (p1x*p2y+p2x*p3y+p3x*p1y)-(p2x*p1y+p3x*p2y+p1x*p3y)
        else:
            return 0
    if p2x==p3x:
        if p1y==p2y:
            return (p1x*p2y+p2x*p3y+p3x*p1y)-(p2x*p1y+p3x*p2y+p1x*p3y)
        if p1y==p3y:
            return (p1x*p2y+p2x*p3y+p3x*p1y)-(p2x*p1y+p3x*p2y+p1x*p3y)
        else:
            return 0
    return 0
maxi=-sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cnt=tri(i,j,k)
            
            maxi=max(maxi,cnt)
print(maxi)