import heapq
import sys

n=int(input())
max_avg=-sys.maxsize
arr=list(map(int,input().split()))
for k in range(1,n-1):
    pq=[]
    
    for i in range(k,n):
        heapq.heappush(pq,arr[i])
    heapq.heapify(pq)
    #print(pq)
    #print(-sum(pq))
    heapq.heappop(pq)
    #print(pq)
    #print(sum(pq)/(n-k-1))
    max_avg=max(max_avg,sum(pq)/(n-k-1))
    
print(f"{max_avg:.2f}")