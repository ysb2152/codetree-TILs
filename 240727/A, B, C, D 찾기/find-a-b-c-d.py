L=list(map(int,input().split()))
L.sort()
A=L[0]
B=L[1]
C=L[2]

if L[3]==A+B:
    D=L[4]
else:
    D=L[3]
print(A,B,C,D)