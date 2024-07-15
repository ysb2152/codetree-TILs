n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
cnt=0
for i in range(0,len(A)):
    if A[i]!=B[i]:
        print("No")
        break
    else:
        cnt+=1
if cnt==len(A):
    print("Yes")