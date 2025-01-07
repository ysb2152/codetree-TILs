n, k = map(int, input().split())
arr = [[0]+list(map(int, input().split())) for _ in range(n)]
prefix=[[0 for _ in range(n+1)]for _ in range(n+1)]
arr=[[0 for _ in range(n+1)]] + arr
answer=[[0 for _ in range(n+1)]for _ in range(n+1)]
max_ans=-999999
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+arr[i][j]
#for ele in prefix:
    #print(ele)
for i in range(1,n-k+2):
    for j in range(1,n-k+2):
        answer[i][j]=prefix[i+k-1][j+k-1]-prefix[i-1][j+k-1]-prefix[i+k-1][j-1]+prefix[i-1][j-1]
for ele in answer:
    max_ans=max(max_ans,max(ele))
    #print(ele)
print(max_ans)