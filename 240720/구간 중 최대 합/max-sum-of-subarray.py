n,k=map(int,input().split())
L=list(map(int,input().split()))
max_sum=0
for i in range(n-k+1):
    cnt=0
    for j in range(i,i+k):
        cnt+=L[j]
    max_sum=max(max_sum,cnt)
print(max_sum)