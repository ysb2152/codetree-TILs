n,k=map(int,input().split())
L=[int(input()) for _ in range(n)]
EXP=[]

for j in range(0,n-3):
    for k in range(j+1,j+4):
        
        if L[j]==L[k]:
            EXP.append(L[j])
if EXP==[]:
    print("-1")
else:
    print(max(EXP))