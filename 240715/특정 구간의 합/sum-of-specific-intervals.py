n,m=map(int,input().split())
A=list(map(int,input().split()))
def check(a,b):
    global A
    cnt=0
    
    C=A[a-1:b]
    
    for ele in C:
        cnt+=ele
    print(cnt)
for _ in range(m):
    a1,b1=map(int,input().split())
    check(a1,b1)