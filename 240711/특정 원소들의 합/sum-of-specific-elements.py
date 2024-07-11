L=[list(map(int,input().split())) for _ in range(4)]
summ=0
for i in range(0,4):
    for j in range(0,i+1):
        summ+=L[i][j]
print(summ)