n,m=map(int,input().split())
ans=[]

def choose(num,cnt):
    if num==m+1:
        for ele in ans:
            print(ele,end=" ")
        print(" ")
        return
    for i in range(cnt,n+1):
        if i not in ans:
            ans.append(i)        
            choose(num+1,i)
            ans.pop()
    return
choose(1,1)