L=[]
chp=0
def comp(n):
    global chp
    if len(L)==1:
        return L[0]
    if n==0:
        return chp
    if L[n-1]>chp:
        chp=L[n-1]
        
        return comp(n-1)
    elif L[n-1]<chp:
            
        return comp(n-1)
    elif L[n-1]==chp:
        
        return comp(n-1)
    
n=int(input())
L=list(map(int,input().split()))
print(comp(n))