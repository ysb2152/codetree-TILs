n=int(input())
L=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        L[i][0]=1
        L[0][j]=1
for i in range(1,n):
    for j in range(1,n):
        L[i][j]=L[i-1][j]+L[i][j-1]+L[i-1][j-1]
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")