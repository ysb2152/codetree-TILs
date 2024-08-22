n,k=map(int,input().split())
arr=list(map(int,input().split()))
hashmap={}
cnt=0
for ele in arr:
    if ele in hashmap:
        hashmap[ele]+=1
    else:
        hashmap[ele]=1
for i in range(n):
    hashmap[arr[i]]-=1
    for j in range(i):
        diff=k-arr[i]-arr[j]
        if diff in hashmap:
            cnt+=hashmap[diff]
print(cnt)