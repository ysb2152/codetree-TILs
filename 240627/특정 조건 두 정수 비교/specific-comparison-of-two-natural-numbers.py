a,b=map(int,input().split())
if a<b:
    print("1",end=" ")
elif b<a:
    print("0",end=" ")
if a==b:
    print("1")
else:
    print("0")