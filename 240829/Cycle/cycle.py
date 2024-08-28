n,p=map(int,input().split())
ans=[]

a=(n*n)%p
ans.append(a)
while True:
    new_a=(a*n)%p
    
    if new_a in ans:
        num=new_a
        break
    ans.append(new_a)
    
    a=new_a
#print(num)
print(len(ans)-ans.index(num))