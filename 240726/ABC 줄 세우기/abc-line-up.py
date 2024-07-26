n=int(input())
L=list(input().split())
cnt=0
for i in range(n-1):
    if ord(L[i])>=ord(L[i+1]):
        a=L[i+1]
        L[i+1]=L[i]
        L[i]=a
        cnt+=1
print(cnt)