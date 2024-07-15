def comp(n):
    if n==0:
        return
    print("* "*n,end=" ")
    print(" ")
    comp(n-1)
def comp1(n):
    if n==0:
        return
    comp1(n-1)
    print("* "*n,end=" ")
    print(" ")
n=int(input())
c=n
comp(n)


comp1(c)