import heapq
n=int(input())
pq=[]
for _ in range(n):
    a=int(input())
    if a==0:
        if len(pq)==0:
            print("0")
            continue
        else:
            print(-heapq.heappop(pq))
            continue
    else:
        heapq.heappush(pq,-a)
        
    #print(pq)