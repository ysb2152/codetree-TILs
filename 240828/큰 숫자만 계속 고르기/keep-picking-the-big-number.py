import heapq
n,m=map(int,input().split())
hq=[]
nums=list(map(int,input().split()))
nums=[-num for num in nums]
heapq.heapify(nums)

for i in range(m):
    a=heapq.heappop(nums)
    a+=1
    heapq.heappush(nums,a)
    #print(nums)
print(-nums[0])