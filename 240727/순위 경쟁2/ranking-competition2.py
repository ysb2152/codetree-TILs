n=int(input())
L=[list(input().split())for _ in range(n)]
A=0
B=0
fame=[]
cnt=0
for i in range(n):
    L[i][1]=int(L[i][1])

for i in range(n):
    beforefame=fame
    if L[i][0]=='A':
        A+=L[i][1]
        if A>B:
            
            fame='A'
        if A<B:
            
            fame=['B']
        if A==B:
            fame=['A','B']
    elif L[i][0]=='B':
        B+=L[i][1]
        if A>B:
            
            fame='A'
        if A<B:
            
            fame=['B']
        if A==B:
            fame=['A','B']
    
    if beforefame!=fame:
        cnt+=1
print(cnt)