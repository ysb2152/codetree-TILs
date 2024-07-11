L=[list(input().split()) for _ in range(5)]


for i in range(0,5):
    for j in range(0,3):
        L[i][j]=L[i][j].upper()
        print(L[i][j],end=" ")
    print(" ")