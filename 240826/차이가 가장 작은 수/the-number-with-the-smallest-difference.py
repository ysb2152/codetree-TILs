import sys
from sortedcontainers import SortedSet
ss=SortedSet()
n,m=map(int,input().split())
L=[]
min_cnt=sys.maxsize
for i in range(n):
    a=int(input())
    ss.add(a)
    L.append(a)
for x in L:
    if ss.bisect_right(x)==len(ss):
        continue
    else:
        
        p=abs(ss[ss.bisect_right(x-m)-1]-x)
        
        if p>=m:
            min_cnt=min(min_cnt,p)
if min_cnt==sys.maxsize:
    print("-1")
else:
    print(min_cnt)