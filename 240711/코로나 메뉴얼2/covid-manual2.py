A=list(input().split())
B=list(input().split())
C=list(input().split())
A[1]=int(A[1])
B[1]=int(B[1])
C[1]=int(C[1])
L=[0 for _ in range(4)]
if A[0]=='Y' and A[1]>=37:
    L[0]+=1
elif A[0]=='N' and A[1]>=37:
    L[1]+=1
elif A[0]=='Y' and A[1]<37:
    L[2]+=1
elif A[0]=='N' and A[1]<37:
    L[3]+=1
if B[0]=='Y' and B[1]>=37:
    L[0]+=1
elif B[0]=='N' and B[1]>=37:
    L[1]+=1
elif B[0]=='Y' and B[1]<37:
    L[2]+=1
elif B[0]=='N' and B[1]<37:
    L[3]+=1
if C[0]=='Y' and C[1]>=37:
    L[0]+=1
elif C[0]=='N' and C[1]>=37:
    L[1]+=1
elif C[0]=='Y' and C[1]<37:
    L[2]+=1
elif C[0]=='N' and C[1]<37:
    L[3]+=1
cnt=0
for ele in L:
    
    print(ele,end=" ")
if L[0]>=2:
    print("E")