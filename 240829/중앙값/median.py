import heapq
t=int(input())
pq=[]
for _ in range(t):
    m=int(input())
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        if i==0:
            heapq.heappush(pq,arr[i])
            print(arr[i],end=" ")
            continue
        if i%2==0:
            heapq.heappush(pq,arr[i])
            print(arr[i//2],end=" ")
            continue
        else:
            heapq.heappush(pq,arr[i])
    print(pq)
    pq=[]