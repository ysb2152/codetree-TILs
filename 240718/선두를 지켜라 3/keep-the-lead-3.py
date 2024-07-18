n,m=map(int,input().split())
A=[]
B=[]
fame=[]
positionA=0
positionB=0
cnt=0
for i in range(n):
    v,t=map(int,input().split())
    for i in range(1,t+1):
        A.append(positionA+v*i)
    positionA=positionA+(v*t)
for i in range(m):
    v,t=map(int,input().split())
    for i in range(1,t+1):
        B.append(positionB+v*i)
    positionB=positionB+(v*t)
if len(A)>len(B):
    for i in range(1,len(B)-1):
        if A[i]<B[i]: 
            fame.append('B')
            break
        if A[i]>B[i]:
            fame.append('A')
            break
        
    for i in range(1,len(B)):
        if A[i]==B[i]:
            fame.append('AB')
        if (A[i-1]<=B[i-1]) and (A[i]>B[i]):
            fame.append('A')
        if (A[i-1]>=B[i-1]) and (A[i]<B[i]):
            fame.append('B')
        
if len(A)<len(B):
    for i in range(1,len(B)-1):
        if A[i]<B[i]: 
            fame.append('B')
            break
        if A[i]>B[i]:
            fame.append('A')
            break
    for i in range(1,len(A)):
        if A[i]==B[i]:
            fame.append('AB')
        if (A[i-1]<=B[i-1]) and (A[i]>B[i]):
            fame.append('A')
        if (A[i-1]>=B[i-1]) and (A[i]<B[i]):
            fame.append('B')
if len(A)==len(B):
    for i in range(1,len(B)-1):
        if A[i]<B[i]: 
            fame.append('B')
            break
        if A[i]>B[i]:
            fame.append('A')
            break
    for i in range(1,len(A)):
        if A[i]==B[i]:
            fame.append('AB')
        if (A[i-1]<=B[i-1]) and (A[i]>B[i]):
            fame.append('A')
        if (A[i-1]>=B[i-1]) and (A[i]<B[i]):
            fame.append('B')
for i in range(1,len(fame)):
    if fame[i-1]!=fame[i]:
        cnt+=1
print(cnt+1)