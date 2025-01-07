N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]
cnt=0
nums=[i for i in range(1,N+1)]
for i in range(len(nums)):
    if nums[i] in missing:
        nums[i]=0
    else:
        nums[i]=1
#print(nums)
prefix=[0 for _ in range(N)]
prefix[0]=nums[0]
for i in range(1,N):
    if nums[i]==1:
        prefix[i]=prefix[i-1]+1
    else:
        prefix[i]=prefix[i-1]
    
print(K-max(prefix))
