def comp(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return comp(n-1)*n
n=int(input())
print(comp(n))