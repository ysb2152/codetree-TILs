def diff(A):
    A=list(A)
    cnt=0
    if A[0]!=A[1]:
        cnt+=1
    for i in range(1,len(A)):
        if A[0]!=A[i]:
            cnt+=1
    return cnt

B=input()

if diff(B)>=1:
    print("Yes")
else:
    print("No")