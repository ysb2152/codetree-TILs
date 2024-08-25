import sys
from sortedcontainers import SortedSet
ss=SortedSet()
n,m=map(int,input().split())

min_cnt=sys.maxsize
for i in range(n):
    a=int(input())
    ss.add(a)
for i in range(n):
    if ss.bisect_right(ss[i])==len(ss):
        continue
    else:
        
        p=abs(ss[ss.bisect_right(ss[i]-m)-1]-ss[i])
        
        if p>=m:
            min_cnt=min(min_cnt,p)
if min_cnt==sys.maxsize:
    print("-1")
else:
    print(min_cnt)