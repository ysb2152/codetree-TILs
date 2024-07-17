n,k=map(int,input().split())
L=[0 for _ in range(n)]
for i in range(k):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        L[j]+=1
print(max(L))