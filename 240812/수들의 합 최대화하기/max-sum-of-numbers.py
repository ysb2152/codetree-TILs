n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0 for _ in range(n)]for _ in range(2)]
ans=[[0 for _ in range(n)]for _ in range(n)]
max_cnt=-9999
def choose(num):
    global ans
    global max_cnt
    if num==n+1:
        cnt=0
        anss=0
        for row in ans:
            cnt+=row.count(1)
        if cnt==n:
            for i in range(n):
                for j in range(n):
                    if ans[i][j]==1:
                        anss+=grid[i][j]
        max_cnt=max(max_cnt,anss)

        
        return
    for i in range(n):
        if visited[0][i]=='V' :
            continue
        for j in range(n):
            if visited[1][j]=='V':
                continue
            visited[0][i]='V'
            visited[1][j]='V'
            ans[i][j]=1
            
            choose(num+1)
            visited[0][i]=0
            visited[1][j]=0
    ans=[[0 for _ in range(n)]for _ in range(n)]
    

    return
choose(1)
print(max_cnt)