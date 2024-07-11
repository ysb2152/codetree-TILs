L=[list(map(int,input().split())) for _ in range(4)]

summ=0
for i in range(0,len(L)):
    summ=0
    for j in range(0,4):
        summ+=L[i][j]
    print(summ)