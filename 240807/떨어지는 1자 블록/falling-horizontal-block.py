n,m,k=map(int,input().split())
L=[list(map(int,input().split()))for _ in range(n)]
flag=False

for i in range(n):
    for j in range(k-1,k-1+m):
        if L[i][j]==1:
            for p in range(k-1,k-1+m):
                L[i-1][p]=1
            flag=True
            break
    if flag:
        break
if not flag:
    for i in range(n):
        for j in range(k-1,k-1+m):
            L[i][j]=1
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")