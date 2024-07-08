n=int(input())
for i in range(1,2*n+1):
    for j in range(1,n+1):
        if i%2==1:
            print(f"{i+8+j*2}",end=" ")
    if i%2==0:
        print("")