n=int(input())
for i in range(1,n+1):
    for j in range(n-i+1,0,-1):
        print("*",end=" ")
    print()
print("",end="")
for i in range(2,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()