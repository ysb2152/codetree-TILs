n=int(input())
for i in range(n):
    for j in range(n+1-i,1,-1):
        print("*",end=" ")
    print()