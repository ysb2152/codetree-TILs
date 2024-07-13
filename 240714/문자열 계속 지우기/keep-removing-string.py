A=input()
B=input()
while B in A:
    if B in A:
        A=A[:A.find(B)]+A[(A.find(B))+len(B):]
print(A)