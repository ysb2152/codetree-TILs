L=tuple(map(int,input().split()))
def iscon(a):
    if (a[0]+a[2])/2==a[1]:
        return True
    else:
        return False
if iscon(L):
    print("0")
for i in range(L[1]+1,L[2]):
    t=[L[1],i,L[2]]
    if iscon(t):
        print("1")
    else:
        for j in range(t[0]+1,t[1]):
            s=[t[0],j,t[1]]
            if iscon(s):
                print("2")