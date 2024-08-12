import sys
n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[False] * (n+1)
ans=[]
max_cnt=-sys.maxsize


def choose(num):
    
    min_cnt=sys.maxsize
    global max_cnt
    if num==n+1:
        
                   
        for j in range(n):
            min_cnt=min(min_cnt,grid[j][ans[j]])
        
        max_cnt=max(max_cnt,min_cnt)
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