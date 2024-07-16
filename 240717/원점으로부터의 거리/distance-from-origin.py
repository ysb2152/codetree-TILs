n=int(input())
class point:
    def __init__(self,x=0,y=0,n=0):
        self.x=x
        self.y=y
        self.n=n
L=[point() for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    L[i].x=a
    L[i].y=b
    L[i].n=i+1
L.sort(key=lambda x: ((abs(x.x)+abs(x.y)),x.n))
for point in L:
    print(f"{point.n}")