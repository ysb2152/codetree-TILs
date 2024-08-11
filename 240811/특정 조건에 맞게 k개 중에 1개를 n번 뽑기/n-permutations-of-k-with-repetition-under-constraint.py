k,n=map(int,input().split())
ans=[]
def choose(num):
    if n==1:
        for j in range(1,k+1):
            print(j)
        return
    if num==n+1:
        for ele in ans:
            print(ele,end=" ")
        print(" ")
        return
    for i in range(1,k+1):
        if len(ans)>=2:
            if ans[-1]==ans[len(ans)-2]==i:
                continue
        ans.append(i)
        
        choose(num+1)
        ans.pop()
    return
choose(1)