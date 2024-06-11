n=input()
n=int(n)
def is_5_mul(n):
    a=n/10
    a=int(a)
    b=n-a*10
    if (a+b)%5==0:
        return True
    else:
        return False
a=is_5_mul(n)
if a==True:
    print("Yes")
else:
    print("No")