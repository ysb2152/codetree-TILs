import heapq
n,m=map(int,input().split())

hq=[]
for _ in range(n):
    a,b=map(int,input().split())
    heapq.heappush(hq,(abs(a)+abs(b),a,b))
    
    
for _ in range(m):
    newhq=[]
    for point in hq:
        _,a,b=point
        heapq.heappush(newhq,((abs(a)+abs(b)),a,b))
    x,y,z=heapq.heappop(newhq)
    
    heapq.heappush(newhq,(x+4,y+2,z+2))
    
    hq=newhq
    
print(hq[0][1],hq[0][2])