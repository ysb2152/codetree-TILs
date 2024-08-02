n=int(input())
L=[list(map(int,input().split()))for _ in range(n)]
max_coin=-9999
def in_range(a,b):
    return 0<=a and a<n and 0<=b and b<n
def coins(a,b):
    coin=0
    for i in range(a,a+2):
        for j in range(b,b+2):
            coin+=1
    return coin
for i in range(n):
    if i+2>=n:
        continue
    for j in range(n):
        if j+2>=n:
            continue
        max_coin=max(max_coin,coins(i,j))
print(max_coin)