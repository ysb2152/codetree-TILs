n,k=map(int,input().split())
hashmap={}
nums=list(map(int,input().split()))
for i in range(n):
    hashmap[nums[i]]=1
cnt=0
for ele in hashmap:
    if k-ele in hashmap:
        cnt+=1
print(cnt//2)