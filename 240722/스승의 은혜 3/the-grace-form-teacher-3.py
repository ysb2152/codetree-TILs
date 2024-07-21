n,b=map(int,input().split())
L=[tuple(map(int,input().split()))for _ in range(n)]

max_num=0

L.sort(key=lambda x: x[0]+x[1])

for i in range(n):
    cnt=0
    num=0
    for j in range(n):
        
        if j==i:
            cnt+=(L[j][0]//2)+L[j][1]
            
            if cnt>b:
                break
            num+=1
            continue
        cnt+=L[j][0]+L[j][1]
        
        
        if cnt>=b:
            
            break
        num+=1
    
    

    
    max_num=max(max_num,num)
    
print(max_num)