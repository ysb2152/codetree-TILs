n=int(input())
ans=[]

def check():
    i=0
    
    while i<n:
        if ans[i:i+ans[i]].count(ans[i])!=ans[i]:
            return False
        else:
            
            i=i+ans[i]
    
    return True
    
    

cnt=0   

def choose(num):
    global cnt
    if num==n+1:
        if check()!=False:
            cnt+=1
        return cnt
    
    for i in range(1,10):
        ans.append(i)
        choose(num+1)
        ans.pop()
    return
choose(1)
print(cnt)