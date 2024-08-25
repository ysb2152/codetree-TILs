import sys
from sortedcontainers import SortedSet
n,m=map(int,input().split())
L=[]
for _ in range(n):
    a=tuple(map(int,input().split()))
    L.append(a)
ss=SortedSet(L)

for _ in range(m):
    k=int(input())
    k=(k,1)
    index=ss.bisect_left(k)
    if index==len(ss):
        print("-1 -1")
    else:
        print(ss[index][0],ss[index][1])
        ss.remove(ss[index])