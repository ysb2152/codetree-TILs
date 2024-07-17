n=int(input())
L=[[0 for _ in range(200)]for _ in range(200)]
offset=100
for i in range(0,n):
    x1,y1,x2,y2=tuple(map(int,input().split()))
    x1,y1,x2,y2=x1+offset,y1+offset,x2+offset,y2+offset
    if i%2==0:
        for a in range(x1,x2):
            for b in range(y1,y2):
                L[a][b]=1
    else:
        for a in range(x1,x2):
            for b in range(y1,y2):
                L[a][b]=2
cnt=0
for row in L:
    for ele in row:
        if ele==2:
            cnt+=1
print(cnt)