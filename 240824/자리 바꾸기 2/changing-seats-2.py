n,k=map(int,input().split())
L=[]
for i in range(0,n+1):
    L.append(i)
L1=[set([i])for i in range(1,n+1)]
orders=[tuple(map(int,input().split()))for _ in range(k)]

for _ in range(3):
    for i in range(k):
        a,b=orders[i]
        a,b=a-1,b-1
        L[a],L[b]=L[b],L[a]
        L1[L[a]].add(a+1)
        L1[L[b]].add(b+1)
for row in L1:
    print(len(row))