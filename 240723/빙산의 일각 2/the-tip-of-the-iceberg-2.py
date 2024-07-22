n=int(input())
H=[]
for _ in range(n):
    a=int(input())
    H.append(a)
Hs=[0 for _ in range(n)]
max_cnt=-9999999
def sink(H,k):
    P=[]
    for ele in H:
        P.append(ele-k)
    return P
for i in range(0,max(H)):
    after=sink(H,i)
    for j in range(len(after)):
        if after[j]<0:
            after[j]=0
    
    cnt=0
    for t in range(len(after)-1):
        if 0 not in after:
            cnt+=1
            break
            
        if after[0]==0:
            if after[t]==0 and after[t+1]>0:
                cnt+=1
        elif after[0]!=0:
            if t==0:
                cnt+=1
            
            if after[t]==0 and after[t+1]>0:
                cnt+=1
            
        
    max_cnt=max(max_cnt,cnt)
print(max_cnt)