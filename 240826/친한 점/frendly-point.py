from sortedcontainers import SortedSet
ss=SortedSet()
n,m=map(int,input().split())
for _ in range(n):
    a=tuple(map(int,input().split()))
    ss.add(a)
for _ in range(m):
    x,y=map(int,input().split())
    if ss.bisect_left((x,y))==len(ss):
        print("-1 -1")
        continue
    else:
        a,b=ss[ss.bisect_left((x,y))]
        print(a,b)