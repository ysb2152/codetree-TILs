N=input()
N=int(N)
def div(N):
    k=0
    for i in range(1,N+1):
      k=k+i
    k=k/10
    return k
a=div(N)
a=int(a)
print(f"{a}")