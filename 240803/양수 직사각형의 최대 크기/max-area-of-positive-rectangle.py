n,m=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
max_size=-99999
def alltrue(a,b,c,d):
    for i in range(a,c+1):
        for j in range(b,d+1):
            if L[i][j]<0:
                return 0
    return (c-a+1)*(d-b+1)
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1,n):
            for y2 in range(y1,m):
                max_size=max(max_size,alltrue(x1,y1,x2,y2))
print(max_size)