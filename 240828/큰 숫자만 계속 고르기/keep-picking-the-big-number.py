import heapq
n,m=map(int,input().split())
hq=[]
nums=list(map(int,input().split()))
for i in range(n):
    heapq.heappush(hq,-nums[i])

for i in range(m):
   
    hq[0]+=1
    if hq[0]>min(hq):
        heapq.heapify(hq)
print(-hq[0])