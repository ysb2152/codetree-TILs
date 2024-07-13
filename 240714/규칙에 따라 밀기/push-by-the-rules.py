A=input()
B=input()
B=list(B)
for i in range(0,len(B)):
    if B[i]=='L':
        A=A[1:]+A[0]
        
    if B[i]=='R':
        A=A[len(A)-1]+A[:len(A)-1]
print(A)