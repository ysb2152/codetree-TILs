A=input()
B=input()
n=0
for i in range(0,len(A)):
    C=A[i+1:]+A[:i+1]
    
    n+=1
    if C==B:
        break
if n>=len(A):
    print("-1")
else:
    print(n)