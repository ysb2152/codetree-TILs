n=int(input())
cost=[list(map(int,input().split()))for _ in range(n)]
visited=[False] * (n+1)
min_cost=9999
ans=[]
def choose(num):
    global min_cost
    if num==n+1:
        if ans[0]!=1:
            return
        else:
            #print(ans)
            costs=0
            for j in range(n-1):
                #print(ans[j]-1,ans[j+1]-1)
                if cost[ans[j]-1][ans[j+1]-1]==0:
                    return
                costs+=cost[ans[j]-1][ans[j+1]-1]
            if cost[ans[-1]-1][0]==0:
                return
            costs+=cost[ans[-1]-1][0]
            #print(costs)
            min_cost=min(min_cost,costs)

        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i]=True
        ans.append(i)
        choose(num+1)
        ans.pop()
        visited[i]=False
    return
choose(1)
print(min_cost)