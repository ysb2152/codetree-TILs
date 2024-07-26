n=int(input())
L=[list(input().split())for _ in range(n)]
A=0
B=0
C=0
fame=['A','B','C']
cnt=0
for i in range(n):
    L[i][1]=int(L[i][1])

for i in range(n):
    
    beforefame=fame
    
    if L[i][0]=='A':
        A+=L[i][1]
        if A>B>C:
            fame=['A']
        if A<C<B:
            fame=['B']
        if A<B<C:
            fame=['C']
        if A==B and B<C:
            fame=['C']
        if A==B and B>C:
            fame=['A','B']
        if B==C and B<A:
            fame=['A']
        if B==C and B>A:
            fame=['B','C']
        if A==C and A<B:
            fame=['B']
        if A==C and A>B:
            fame=['A','C']
        if A==B==C:
            fame=['A','B','C']
    elif L[i][0]=='B':
        B+=L[i][1]
        if A>B>C:
            fame=['A']
        if A<C<B:
            fame=['B']
        if A<B<C:
            fame=['C']
        if A==B and B<C:
            fame=['C']
        if A==B and B>C:
            fame=['A','B']
        if B==C and B<A:
            fame=['A']
        if B==C and B>A:
            fame=['B','C']
        if A==C and A<B:
            fame=['B']
        if A==C and A>B:
            fame=['A','C']
        if A==B==C:
            fame=['A','B','C']
    elif L[i][0]=='C':
        C+=L[i][1]
        if A>B>C:
            fame=['A']
        if A<C<B:
            fame=['B']
        if A<B<C:
            fame=['C']
        if A==B and B<C:
            fame=['C']
        if A==B and B>C:
            fame=['A','B']
        if B==C and B<A:
            fame=['A']
        if B==C and B>A:
            fame=['B','C']
        if A==C and A<B:
            fame=['B']
        if A==C and A>B:
            fame=['A','C']
        if A==B==C:
            fame=['A','B','C']
    
    if beforefame!=fame:
        cnt+=1
print(cnt)