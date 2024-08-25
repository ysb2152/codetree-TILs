from sortedcontainers import SortedSet
ss=SortedSet()
n,m=map(int,input().split())
L=list(map(int,input().split()))
for i in range(n):
    ss.add(L[i])
for _ in range(m):
    a=input()
    a=int(a)
    if ss.bisect_left(a)==len(ss):
        print("-1")
    else:
        print(ss[ss.bisect_left(a)])