L=list(map(int,input().split()))
L.sort()
A=L[0]
B=L[1]
C=L[2]

if L[2]==A+B:
    C=L[3]
else:
    C=L[2]
D=L[-1]-A-B-C
print(A,B,C,D)