n,m=map(int,input().split())
L=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b=tuple(map(int,input().split()))
    L[a-1][b-1]=a*b
for row in L:
    for ele in row:
        print(ele,end=" ")
    print(" ")