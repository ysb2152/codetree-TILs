n=int(input())
L=input()
def check(L,i,j):
    tocheck=L[i:j+1]
    L=L[:j-1]+L[j:]
    if tocheck in L:
        return 0
    else:
        return len(tocheck)
min_size=9999
check0=[]
check1=[]
final=[]
for i in range(len(L)):
    
    for j in range(i+1,len(L)):
        
        
        if L[i:j+1] in L:
            if check(L,i,j)==0:
                check0.append(len(L[i:j+1]))
                
                continue
            else:
                size=check(L,i,j)
                check1.append(size)
                continue
for ele in check1:
    if ele not in check0:
        final.append(ele)
final1=[]
for ele in final:
    if ele not in final1:
        final1.append(ele)



print(min(final1))