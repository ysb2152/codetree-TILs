import heapq
n,m=map(int,input().split())

hq=[]
for _ in range(n):
    a,b=map(int,input().split())
    heapq.heappush(hq,(abs(a)+abs(b),a,b))
    
    
for _ in range(m):
    
    x,y,z=heapq.heappop(hq)
    
    heapq.heappush(hq,(x+4,y+2,z+2))
    
    
    
print(hq[0][1],hq[0][2])