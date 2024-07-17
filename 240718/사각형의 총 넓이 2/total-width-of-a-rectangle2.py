n=int(input())
offset=100
cnt=0
L=[[0 for _ in range(200)]for _ in range(200)]
for _ in range(n):
    x1,y1,x2,y2=tuple(map(int,input().split()))
    x1+=offset
    x2+=offset
    y1+=offset
    y2+=offset
    for i in range(x1,x2):
        for j in range(y1,y2):
            L[i][j]=1
cnt=0
for row in L:
    for ele in row:
        if ele==1:
            cnt+=1
print(cnt)