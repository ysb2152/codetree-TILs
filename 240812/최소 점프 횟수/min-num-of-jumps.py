n=int(input())
line=list(map(int,input().split()))
ans=[0]
min_jump=99999
r=0
def choose(num):
    global min_jump
    
    if len(ans)>=1 and ans[-1]>=n-1:
        #print(" ")
        
        min_jump=min_jump=min(min_jump,len(ans)-1)
        return 
    
    for i in range(1,line[num]+1):
        new_num=num+i
        ans.append(num+i)
        #print(num+i)
        choose(new_num)
        ans.pop()
    
    return 
choose(0)
if min_jump==99999:
    print("-1")
else:
    print(min_jump)