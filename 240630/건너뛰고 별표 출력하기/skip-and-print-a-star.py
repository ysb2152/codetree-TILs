n=int(input())

for i in range(1,2*n+1):
    if i%2==0:
        print()
    else:
     for _ in range((i+1)//2):
        print("*",end="")
     print()

for i in range((n-1)*2,0,-1):
    if i==(n-1)*2:
        continue
    if i%2==0:
        print()
    else:
        for _ in range((i//2)+1):
            print("*",end="")
        print()