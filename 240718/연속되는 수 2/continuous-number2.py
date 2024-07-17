n=int(input())
cnt=0
L=[]
for i in range(n):
    a=int(input())
    L.append(a)
for i in range(n):
    if i==0 or L[i]==L[i-1]:
        cnt+=1
print(cnt)