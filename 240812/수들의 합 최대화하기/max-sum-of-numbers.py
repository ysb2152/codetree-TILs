n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[False] * (n+1)
ans=[]

max_cnt=-9999
def choose(num):
    
    global max_cnt
    
    if num==n+1:
        
        cnt=0
    
        for j in range(n):
            cnt+=grid[j][ans[j]]
        max_cnt=max(max_cnt,cnt)
        
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i]=True
        ans.append(i)
        choose(num+1)
        ans.pop()
        visited[i]=False

    return
choose(1)
print(max_cnt)