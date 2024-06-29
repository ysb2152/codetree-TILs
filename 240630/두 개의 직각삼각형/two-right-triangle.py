n=int(input())
for i in range(2*n):
    print("*",end="")
print()
for i in range(1,n+1):
    for j in range (n-i):
        print("*",end="")
    for j in range (2*i):
        print(" ",end="")
    for j in range (n-i):
        print("*",end="")
    print()