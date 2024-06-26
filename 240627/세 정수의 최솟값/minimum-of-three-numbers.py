a,b,c=map(int,input().split())
if a<=b and a<=c:
    print(f"{a}")
elif a>=b and c>=b:
    print(f"{b}")
else:
    print(f"{c}")