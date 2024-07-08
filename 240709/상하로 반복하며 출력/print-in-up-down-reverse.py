n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==1:
            print(f"{i}",end="")
        else:
            print(f"{4-i+1}",end="")
    print(" ")