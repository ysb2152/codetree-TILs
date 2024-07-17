n=int(input())
offset=100
L=[0 for _ in range(200)]
for i in range(n):
    x1,x2=map(int,input().split())
    x1+=offset
    x2+=offset
    for j in range(x1,x2):
        L[j]+=1
print(max(L))