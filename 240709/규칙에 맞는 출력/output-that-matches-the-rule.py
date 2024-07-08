n=int(input())
cnt=n
for i  in range(n,0,-1):
    for j in range(i,n+1):
        print(f"{j}",end=" ")
    print(" ")