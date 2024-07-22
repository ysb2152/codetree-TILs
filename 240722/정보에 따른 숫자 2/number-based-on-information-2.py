t,a,b=map(int,input().split())
comb=[]
cnt=0
jha=[0 for _ in range(2000)]
for i in range(t):
    L1,L2=tuple(input().split())
    jha[int(L2)]=L1
    comb.append((L1,int(L2)))

comb.sort(key=lambda x:x[1])


def closest(comb,x,alpha):
    
    if alpha=='N':
        pos=[]
        min_dis=99999999
        for i in range(len(comb)):
            if comb[i]=='N':
                pos.append(i)
        for ele in pos:
            min_dis=min(min_dis,abs(ele-x))
        return min_dis
    if alpha=='S':
        pos=[]
        min_dis=9999999
        for i in range(len(comb)):
            if comb[i]=='S':
                pos.append(i)
        
        for ele in pos:
            min_dis=min(min_dis,abs(ele-x))
        return min_dis
for i in range(a,b+1):
    if closest(jha,i,'N')>=closest(jha,i,'S'):
        cnt+=1
print(cnt)