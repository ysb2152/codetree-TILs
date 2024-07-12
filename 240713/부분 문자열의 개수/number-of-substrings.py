A=input()
B=input()
cnt=0
for _ in range(1000):
    if B in A:
        cnt+=1
        A=A[A.find(B)+1:]
        
    
print(cnt)