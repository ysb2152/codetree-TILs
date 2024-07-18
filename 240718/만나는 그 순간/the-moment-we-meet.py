n,m=map(int,input().split())
A=[]
B=[]
positionA=0
positionB=0
for _ in range(n):
    direction,time=input().split()
    time=int(time)
        
    if direction=='L':
        for i in range(time):
            positionA-=1
            A.append(positionA)
    if direction=='R':
        for i in range(time):
            positionA+=1
            A.append(positionA)
for _ in range(m):
    direction,time=input().split()
    time=int(time)
        
    if direction=='L':
        for i in range(time):
            positionB-=1
            B.append(positionB)
    if direction=='R':
        for i in range(time):
            positionB+=1
            B.append(positionB)
if len(A)>len(B):
    for i in range(len(B)):
        if A[i]==B[i]:
            print(i+1)
            break
if len(A)<len(B):
    for i in range(len(A)):
        if A[i]==B[i]:
            print(i+1)
            break
else:
    for i in range(len(A)):
        if A[i]==B[i]:
            print(i+1)
            break