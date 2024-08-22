n,k=map(int,input().split())
hashmap={}
nums=list(map(int,input().split()))
for i in range(n):
    hashmap[nums[i]]=0
for i in range(n):
    hashmap[nums[i]]+=1
cnt=0
for ele in hashmap:
    if k-ele in hashmap:
        if hashmap[ele]>=2:
            cnt+=(hashmap[ele]*(hashmap[ele]-1))//2
        else:
            cnt+=1


        
print(cnt//2)