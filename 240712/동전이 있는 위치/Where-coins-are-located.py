n,m=map(int,input().split())

k=[[0 for _ in range (n)] for _ in range(n)]
for _ in range(m):
    a,b=tuple(map(int,input().split()))
    k[a-1][b-1]=1
for row in k:
    for ele in row:
        print(ele,end=" ")
    print(" ")