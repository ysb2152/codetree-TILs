from sortedcontainers import SortedSet
n,m=map(int,input().split())
arr=list(map(int,input().split()))
ss=SortedSet(arr)

nums=list(map(int,input().split()))
for i in range(m):
    num=nums[i]
    if len(ss)==0:
        print("-1")
        continue
    elif num>ss[-1]:
        
        print(ss[-1])
        ss.remove(ss[-1])
        continue
     
    
    elif num<ss[0]:
        print("-1")
        continue
    elif num in ss:
        print(num)
        ss.remove(num)
        continue
    else:
        print(ss[ss.bisect_left(num)-1])
        ss.remove(ss[ss.bisect_left(num)-1])