import sys
n,m=map(int,input().split())
L=[tuple(map(int,input().split()))for _ in range(n)]
min_dist=sys.maxsize
ans=[]
ans2=[]
def choose2(nums,cnts):
   
    global min_dist
    if nums==3:
        
        x1,y1=L[ans[ans2[0]]]
        x2,y2=L[ans[ans2[1]]]
        dist=(((x1-x2)**2)+((y1-y2)**2))
        min_dist=min(min_dist,dist)

        return
    for i in range(cnts,len(ans)):
        if i not in ans2:
            ans2.append(i)
            choose2(nums+1,i)
            ans2.pop()
    return
    
    
    


def choose(num,cnt):
    
    if num==m+1:
        
        choose2(1,0)
                
        return
    for i in range(cnt,n):
        if i not in ans:
            ans.append(i)
            choose(num+1,i)
            ans.pop()
    return
choose(1,0)
print(int(min_dist))