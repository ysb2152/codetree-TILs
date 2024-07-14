def isT(a,b):
    if b[0] in a:
        k=a[a.index(b[0]):a.index(b[0])+len(b)]
        if k==b:
            return True
        else:
            return False
n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if isT(A,B)==True:
    print("Yes")
else:
    print("No")