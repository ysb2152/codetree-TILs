n=int(input())
L=[[0 for _ in range(n)] for _ in range(n)]
for i in range(0,n):
    L[i][0]=i
for i in range(n):
    
    print((L[i][0])+1,end=" ")
    for j in range(1,n):
        L[i][j]=L[i][0] + (n * j)+1
        print(L[i][j],end=" ")
    print(" ")