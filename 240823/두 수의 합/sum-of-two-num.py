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
        if ele==k-ele:
            cnt+=(hashmap[ele]*(hashmap[ele]-1))//2
            hashmap[ele]=0
            
        else:

            cnt+=hashmap[ele]*hashmap[k-ele]
            hashmap[ele]=0
            hashmap[k-ele]=0


        
print(int(cnt))