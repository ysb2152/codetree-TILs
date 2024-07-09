start,end=map(int,input().split())
cnt1=0

for i in range(start+1,end):
    cnt=0
    for j in range(1,i):
        if i%j==0:
            cnt+=j
                    
        if cnt==i and j==i-1 :
            cnt1+=1
            
            break
            
            
print(cnt1)