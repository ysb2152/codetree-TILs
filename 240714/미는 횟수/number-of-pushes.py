A=input()
B=input()
n=0
for i in range(0,len(A)):
    
    A=A[len(A)-1]+A[:len(A)-1]
    
    n+=1
    if A==B:
        break   
    
if n>=len(A):
    print("-1")
else:
    print(n)