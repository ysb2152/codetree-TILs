import heapq
import sys

n=int(input())
max_avg=-sys.maxsize
pq=[]
arr=list(map(int,input().split()))
for i in range(n-2,n):
    heapq.heappush(pq,arr[i])
#print(pq)
sums=sum(pq)
for k in range(n-3,-1,-1):
    heapq.heappush(pq,arr[k])
    #print(pq)
    #heapq.heapify(pq)
    #print(pq)
    sums+=arr[k]
    a=heapq.heappop(pq)
    sums-=a
    #print(pq)
    #print(sum(pq)/(n-k-1))
    max_avg=max(max_avg,sums/(n-k-1))
    heapq.heappush(pq,a)
    sums+=a
    
print(f"{max_avg:.2f}")