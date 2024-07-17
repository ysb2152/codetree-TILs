n=int(input())
L=[[0 for _ in range(200)]for _ in range(200)]
offset=100
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    a,b=a+offset,b+offset
    for i in range(a,a+8):
        for j in range(b,b+8):
            L[i][j]+=1

cnt=0
pure=0
for row in L:
    for ele in row:
        if ele==1:
            cnt+=1
        if ele!=0 and ele!=1:
            cnt+=1
print(cnt)