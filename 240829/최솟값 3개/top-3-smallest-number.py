import heapq
n=int(input())
arr=list(map(int,input().split()))
pq=[]
for i in range(n):
    heapq.heappush(pq,arr[i])
    if len(pq)<3:
        print("-1")
    else:
        print(pq[0]*pq[1]*pq[2])