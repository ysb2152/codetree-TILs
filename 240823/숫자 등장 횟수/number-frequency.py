n,m=map(int,input().split())
hashmap={}
nums=list(map(int,input().split()))
for ele in nums:
    hashmap[ele]=0
for ele in nums:
    hashmap[ele]+=1
orders=list(map(int,input().split()))
for i in range(len(orders)):
    if orders[i] in hashmap:
        print(hashmap[orders[i]],end=" ")
    else:
        print("0",end=" ")