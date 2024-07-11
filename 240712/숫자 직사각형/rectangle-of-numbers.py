n,m=map(int,input().split())
L=[[0 for _ in range(m)] for _ in range(n)]
cnt=1
for i in range(n):
    for j in range(m):
        (L[i][j]) = cnt
        print(L[i][j],end=" ")
        cnt+=1
    print(" ")