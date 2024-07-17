n=int(input())
L=[0 for _ in range(100)]

for _ in range(n):
    x1,x2=map(int,input().split())
    for i in range(x1,x2+1):
        
        L[i-1]+=1
print(max(L))