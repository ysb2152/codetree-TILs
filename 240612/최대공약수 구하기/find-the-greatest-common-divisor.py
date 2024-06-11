n,m=input().split()
n=int(n)
m=int(m)
k=0
for i in range(1,101):
  if i==n or i==m:
    if n==m:
        i=n
    else:
        break
  if (n%i)==0 & (m%i)==0:
    k=i
    

print(k)