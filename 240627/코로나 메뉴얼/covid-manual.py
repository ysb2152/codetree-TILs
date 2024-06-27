A=list(input().split())
B=list(input().split())
C=list(input().split())
A[1]=int(A[1])
B[1]=int(B[1])
C[1]=int(C[1])
cnt=0
if A[0]=='Y' and A[1]>=37:   cnt+=1
if B[0]=='Y' and B[1]>=37:   cnt+=1
if C[0]=='Y' and C[1]>=37:   cnt+=1

if cnt>=2:
    print("E")
else:
    print("N")