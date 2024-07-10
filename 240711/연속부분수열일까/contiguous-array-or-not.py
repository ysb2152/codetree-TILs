n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

for i in range(0,n1):
    for j in range(0,n2):
        if A[i]==B[j]:
            
            C=A[i+1:]
            break
for i in range(n1-1,-1,-1):
    for j in range(n2-1,-1,-1):
        if A[i]==B[j]:
            
            D=A[:i]
            break
for ele in C:
    if ele in A:
        A.remove(ele)


for ele in D:
    if ele in A:
        A.remove(ele)

if A==B:
    print("Yes")
else:
    print("No")