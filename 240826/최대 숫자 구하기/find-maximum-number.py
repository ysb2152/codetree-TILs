from sortedcontainers import SortedSet
ss=SortedSet()
n,m=map(int,input().split())
for i in range(1,m+1):
    ss.add(i)
L=list(map(int,input().split()))
for i in range(n):
    a=L[i]
    ss.remove(a)
    print(ss[-1])