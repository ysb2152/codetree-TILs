L=list(map(int,input().split()))
L.sort()
A=L[0]
B=L[1]
if L[2]==A+B:
    C=L[3]
else:
    C=L[2]
print(A,B,C)