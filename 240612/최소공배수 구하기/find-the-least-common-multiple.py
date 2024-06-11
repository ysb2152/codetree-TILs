n,m=tuple((input().split()))
n=int(n)
m=int(m)
def lcm(n,m):
    for i in range(1,10001):
        if (i%n)==0 and (i%m)==0:
          print(i)
          break
lcm(n,m)