L=list(map(int,input().split()))

cnt=0
L.sort()
if L[0]+1==L[1] and L[1]+1==L[2]:
    print("0")
elif L[0]+2==L[1] or L[1]+2==L[2]:
    print("1")
else:
    print("2")