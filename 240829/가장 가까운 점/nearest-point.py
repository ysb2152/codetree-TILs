import heapq
n,m=map(int,input().split())
arr=[tuple(map(int,input().split()))for _ in range(n)]
hq=[]
for point in arr:
    a,b=point
    heapq.heappush(hq,(abs(a)+abs(b),a,b))
    heapq.heapify(hq)
    
for _ in range(m):
    newhq=[]
    for point in hq:
        _,a,b=point
        heapq.heappush(newhq,(abs(a)+abs(b),a,b))
        
    newhq[0]=list(newhq[0])
    newhq[0][1]+=2
    newhq[0][2]+=2
    newhq[0][0]=abs(newhq[0][1])+abs(newhq[0][2])
    newhq[0]=tuple(newhq[0])
    heapq.heapify(newhq)
    hq=newhq
print(hq[0][1],hq[0][2])