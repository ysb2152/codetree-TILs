n=int(input())
L=list(map(int,input().split()))
minimum=L[1]-L[0]
for i in range(1,n):
    if minimum>(L[i]-L[i-1]):
        minimum=L[i]-L[i-1]
print(minimum)