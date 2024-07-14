n,m=map(int,input().split())
A=list(map(int,input().split()))

def form(m,n,A):
    cnt=0
    
    while m!=1:
        if m%2==1:
            cnt+=A[m-1]
            m-=1
            
        if m%2==0:
            
            cnt+=A[m-1]
            m//=2
    cnt+=A[0]
    return cnt
print(form(m,n,A))