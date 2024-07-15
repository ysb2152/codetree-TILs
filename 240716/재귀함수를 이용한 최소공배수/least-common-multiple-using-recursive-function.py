n=int(input())
L=list(map(int,input().split()))
G=L[0]
def GCD(a,b):
    k=a*b
    if a>b:
        while b>0:
            a,b=b,a%b
        return k//a
    if a<b:
        while a>0:
            a,b=b%a,a
        return k//b
   
def comp(n):
    global G
    if n==1:
        return G
    G=GCD(L[n-1],G)
    
    return comp(n-1) 
print(comp(n))