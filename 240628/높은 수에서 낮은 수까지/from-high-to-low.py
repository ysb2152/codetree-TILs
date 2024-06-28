a,b=map(int,input().split())
if a<b:
    for i in range(b,a-1,-1):
        print(f"{i}",end=" ")
if a>b:
    for i in range(a,b-1,-1):
        print(f"{i}",end=" ")
if a==b:
    print(f"{a}")