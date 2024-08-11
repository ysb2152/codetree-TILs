n=int(input())
ans=[]
real_ans=[]
visited=[False] * (n+1)
def choose(num):
    
    if num==n+1:
        L=[]
        for ele in ans:
            L.append(ele)
        real_ans.append(L)

        
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
real_ans.sort(reverse=True)
for row in real_ans:
    for ele in row:
        print(ele,end=" ")

    print(" ")