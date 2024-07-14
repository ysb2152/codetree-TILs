def evennum(n):
    if ((n%10)+(n//10))%2==0:
        return True
    else:
        return False
def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return evennum(n)
a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if isprime(i)==True:
        cnt+=1
print(cnt)