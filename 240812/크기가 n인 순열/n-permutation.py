n=int(input())
visited=[False] * (n+1)
ans=[]
def choose(num):
    if num==n+1:
        for ele in ans:
            print(ele,end=" ")
        print(" ")
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