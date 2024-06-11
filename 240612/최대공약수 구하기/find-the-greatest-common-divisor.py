n,m=input().split()
n=int(n)
m=int(m)

def gcd(n,m):
  k=0
  for i in range(1, min(n,m)+1):
   if n%i==0 and m%i==0:
     k=i
  print(k)

gcd(n,m)