a,b,c=map(int,input().split())

if a>=b:
    m=a
    if m>c:
        print(f"{a}")
    else:
        print(f"{c}")
else:
    m=b
    if m>c:
        print(f"{b}")
    else:
        print(f"{c}")