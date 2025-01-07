n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix=[0 for _ in range(n)]
prefix[0]=arr[0]
answer=[0 for _ in range(n)]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
#print(prefix)
for i in range(n-k):
    answer[i]=prefix[i+k-1]-prefix[i]+arr[i]
print(max(answer))
