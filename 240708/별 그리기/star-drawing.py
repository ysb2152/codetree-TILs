n=int(input())
for i in range(1,n+1):
    for _ in range(0,n-i):
        print("",end=" ")
    for _ in range(1,2*i):
        print("*",end="")
    print(" ")

for j in range(n-1,0,-1):
    for _ in range(n-j):
        print("",end=" ")
    for _ in range(1,2*j):
        print("*",end="")
    print(" ")