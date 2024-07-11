n,m=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]
C=[[0 for _ in range(m)] for _ in range (n)]
for i in range(n):
    for j in range(m):
        if A[i][j]!=B[i][j]:
            C[i][j]=1
for i in range(n):
    for j in range(m):
        print(C[i][j],end=" ")
    print(" ")