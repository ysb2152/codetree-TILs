def comp(a):
    if a==1:
        return 1
    if a==2:
        return 2
    return comp(a//3)+comp(a-1)
n=int(input())
print(comp(n))