import heapq
import sys
pq=[]
n=int(input())
max_avg=-sys.maxsize
arr=list(map(int,input().split()))
for k in range(1,n-1):
    new_arr=arr[k:]
    for i in range(n-k):
        heapq.heappush(pq,new_arr[i])
    heapq.heapify(pq)
    #print(pq)
    #print(-sum(pq))
    heapq.heappop(pq)
    #print(pq)
    #print(sum(pq)/(n-k-1))
    max_avg=max(max_avg,sum(pq)/(n-k-1))
    pq=[]
print(f"{max_avg:.2f}")