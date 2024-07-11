n,m=map(int,input().split())
L=[[0 for _ in range(m)] for _ in range(n)]
cnt=0
for j in range(m):
    if j%2==0:
        for i in range(n):
            L[i][j]=cnt
            cnt+=1
    if j%2==1:
        for i in range(n-1,-1,-1):
            L[i][j]=cnt
            cnt+=1

for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")