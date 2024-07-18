n,m=map(int,input().split())
A=[]
B=[]
positionA=0
positionB=0
cnt=0
for _ in range(n):
    t,d=input().split()
    t=int(t)
    if d=='L':
        for i in range(1,t+1):
            A.append(positionA-i)
        positionA-=t
    if d=='R':
        for i in range(1,t+1):
            A.append(positionA+i)
        positionA+=t
for _ in range(m):
    t,d=input().split()
    t=int(t)
    if d=='L':
        for i in range(1,t+1):
            B.append(positionB-i)
        positionB-=t
    if d=='R':
        for i in range(1,t+1):
            B.append(positionB+i)
        positionB+=t
if len(A)>len(B):
    for i in range(1,len(B)):
        if (A[i-1]<A[i]) and (B[i-1]>B[i]) and (A[i]==B[i]):
            cnt+=1
        if (A[i-1]>A[i]) and (B[i-1]<B[i]) and (A[i]==B[i]):
            cnt+=1
        
if len(A)<len(B):
    for i in range(1,len(A)):
        if (A[i-1]<A[i]) and (B[i-1]>B[i]) and (A[i]==B[i]):
            cnt+=1
        if (A[i-1]>A[i]) and (B[i-1]<B[i]) and (A[i]==B[i]):
            cnt+=1
if len(A)==len(B):
        if (A[i-1]<A[i]) and (B[i-1]>B[i]) and (A[i]==B[i]):
            cnt+=1
        if (A[i-1]>A[i]) and (B[i-1]<B[i]) and (A[i]==B[i]):
            cnt+=1
      

print(cnt+1)