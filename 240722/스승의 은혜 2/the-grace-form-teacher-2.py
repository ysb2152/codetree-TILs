n,b=map(int,input().split())
L=[]
max_num=0
for _ in range(n):
    a=int(input())
    L.append(a)

for i in range(n):
    cnt=0
    num=0
    for j in range(n):
        
        if j==i:
            cnt+=(L[i]//2)
            num+=1
            
            continue
        cnt+=L[j]
           
        if cnt>b:
            
            break
        num+=1
    
    

    
    max_num=max(max_num,num)
    
print(max_num)