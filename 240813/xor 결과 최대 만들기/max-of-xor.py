import sys
n,m=map(int,input().split())
L=list(map(int,input().split()))
ans=[]
max_ans=-sys.maxsize
def choose(num,cnt):
    global max_ans
    if n==m:
        sums=L[0]
        for j in range(1,m):
            sums=sums^L[j]
        max_ans=max(max_ans,sums)
        return
    if num==m+1:
        
        sums=ans[0]
        for j in range(1,m):
            sums=sums^ans[j]
        max_ans=max(max_ans,sums)
        return
    for i in range(cnt,n):
        if L[i] not in ans:
            ans.append(L[i])
            choose(num+1,i)
            ans.pop()
    return
choose(1,0)
print(max_ans)