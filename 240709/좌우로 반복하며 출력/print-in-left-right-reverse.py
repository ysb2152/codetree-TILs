n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==1:
            print(f"{j}",end="")
        else:
            print(f"{n-j+1}",end="")
    print(" ")