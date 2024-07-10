n=int(input())
L=list(map(int,input().split()))
K=[ele * ele for ele in L]
for ele in K:
    print(f"{ele}",end=" ")