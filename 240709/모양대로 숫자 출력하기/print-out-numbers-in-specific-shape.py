n=int(input())
for i in range(0,n):
    print(" "*i,end="")
    for j in range(n,0,-1):
        if j<=n-i:
            print(f"{j}",end=" ")
        else:
            print("",end=" ")
        
    print(" ")