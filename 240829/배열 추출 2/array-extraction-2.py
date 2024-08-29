import heapq
n=int(input())
pq=[]
for _ in range(n):
    a=int(input())
    if a!=0:
        heapq.heappush(pq,(abs(a),a))
    else:
        if len(pq)==0:
            print("0")
        else:
            abss,x=heapq.heappop(pq)
            print(x)