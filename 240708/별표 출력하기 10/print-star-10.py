n=int(input())
for i in range(0,2*n):
    if i%2==1:
        for _ in range (n-(i-1)//2):
            print("*",end=" ")
    if i%2==0:
        for _ in range((1+(i//2))):
            print("*",end=" ")
    print(" ")