n=int(input())

for i in range(1,n+1):
    if i%2==1:
        print("*",end="")
    else:
        for _ in range(i):
            print("*",end=" ")
    print(" ")