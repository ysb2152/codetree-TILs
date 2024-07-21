n,k=map(int,input().split())
L=[int(input()) for _ in range(n)]
EXP=[]

for j in range(n):
    for k in range(j+1,j+k+1):
        if k>n-1:
            continue
        
        if L[j]==L[k]:
            EXP.append(L[j])

if EXP==[]:
    print("-1")
else:
    print(max(EXP))