from sortedcontainers import SortedSet
ss=SortedSet()
n=int(input())
L=list(map(int,input().split()))
ss.add(0)
min_cnt=9999
for i in range(n):
    ss.add(L[i])
    #print(ss)
    a=ss.bisect_right(L[i])
    if a==len(ss):
        
        min_cnt=min(min_cnt,abs(ss[a-1]-ss[a-2]))
    else:
        #print(ss[a-1],ss[a])
        min_cnt=min(min_cnt,abs(ss[a-2]-L[i]),abs(ss[a]-L[i]))
    print(min_cnt)