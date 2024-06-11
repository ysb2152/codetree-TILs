n,m=input().split()
n=int(n)
m=int(m)
k=0
for i in range(1,101):
  if i==n or i==m:
    if n==m:
        i=n
    if n==1 or m==1:
        k=1
    else:
        break
  if i>n or i>m:
    i=1
  if (n%i)==0 & (m%i)==0:
    k=i
    

print(k)