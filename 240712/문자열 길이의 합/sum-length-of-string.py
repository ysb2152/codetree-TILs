n=int(input())
L=[input() for _ in range(n)]
cnt=0
a=0
for i in range(0,n):
    cnt+=len(L[i])
    if L[i][0]=='a':
        a+=1
print(cnt,end=" ")
print(a)