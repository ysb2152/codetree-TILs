from sortedcontainers import SortedSet
n,m=map(int,input().split())
arr=list(map(int,input().split()))
ss=SortedSet(arr)

nums=list(map(int,input().split()))
for i in range(m):
    num=nums[i]
    if ss.bisect_right(num)==len(ss) or ss.bisect_right(num)==0:
        print("-1")
        continue
    else:
        print(ss[ss.bisect_right(num)-1])
        ss.remove(ss[ss.bisect_right(num)-1])