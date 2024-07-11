L=[[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    L[i][0]=1
    L[0][i]=1
for i in range(1,5):
    for j in range(1,5):
        L[i][j]=L[i-1][j]+L[i][j-1]
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")