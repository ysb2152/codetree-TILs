n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==0 or (j%2==1 and i<=j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")