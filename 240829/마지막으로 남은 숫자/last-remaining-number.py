import heapq
n=int(input())
pq=[]
arr=list(map(int,input().split()))
for i in range(n):
    a=arr[i]
    heapq.heappush(pq,-a)
while len(pq)>=2:
    a=-heapq.heappop(pq)
    b=-heapq.heappop(pq)
    if a==b:
        continue
    else:
        ans=abs(a-b)
        heapq.heappush(pq,-ans)
if len(pq)==1:
    print(-pq[0])
else:
    print("-1")