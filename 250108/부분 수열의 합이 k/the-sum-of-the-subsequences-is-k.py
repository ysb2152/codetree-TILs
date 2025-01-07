n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix=[0 for _ in range(n)]
prefix[0]=arr[0]
answer=[0 for _ in range(n)]
cnt=0
for i in range(n):
    prefix[i]=prefix[i-1]+arr[i]
for i in range(n):
    for j in range(n):
        if k==prefix[i]-prefix[j]+arr[j]:
            cnt+=1
print(cnt)