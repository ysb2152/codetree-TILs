n=int(input())
L=[list(map(int,input().split())) for _ in range(n)]

max_coin=-9999
for row in range(n):
    if row+2>=n:
        continue
    for col in range(n):
        if col+2>=n:
            continue
        coins=0
        for i in range(row,row+3):
            for j in range(col,col+3):
                coins+=L[i][j]
        max_coin=max(max_coin,coins)
print(max_coin)

