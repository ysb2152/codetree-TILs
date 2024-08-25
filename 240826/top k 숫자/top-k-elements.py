from sortedcontainers import SortedSet
ss=SortedSet()
n,k=map(int,input().split())
L=list(map(int,input().split()))
for i in range(n):
    ss.add(L[i])
for i in range(k):
    print(ss[len(ss)-i-1],end=" ")