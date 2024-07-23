n=int(input())
L=input()
L=list(map(int,str(L)))
dis=-9999
def distance(L):
    min_dis=9999
    for i in range(len(L)):
        cnt=0
        if L[i]==1:
        
            for j in range(i+1,len(L)):
                if j==len(L)-1 and L[j]==0:
                    break
                if L[j]==1:
                    break
                cnt+=1
        if cnt!=0:  
            min_dis=min(min_dis,cnt)
    return min_dis
for i in range(n):
    if L[i]==0:
        L[i]==1
        dis=max(dis,distance(L))
        L[i]==0
print(dis)