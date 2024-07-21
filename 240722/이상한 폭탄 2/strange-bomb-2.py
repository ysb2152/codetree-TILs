n,k=map(int,input().split())
L=[int(input()) for _ in range(n)]
EXP=[]

for j in range(n):
    for l in range(j+1,j+k+1):
        if l>n-1 or l<0:
            continue
        
        if L[j]==L[l]:
            
            EXP.append(L[l])

if EXP==[]:
    print("-1")
else:
    print(max(EXP))