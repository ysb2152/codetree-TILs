n=int(input())
for i in range(n,0,-1):
    for _ in range(0,n-i):
        print("",end="  ")
    for _ in range(2*i-1):
        print("*",end=" ")
    print(" ")

for j in range(1,n):
    for _ in range(n-j,1,-1):
        print("",end="  ")
    for _ in range(0,2*j+1):
        print("*",end=" ")
    print(" ")