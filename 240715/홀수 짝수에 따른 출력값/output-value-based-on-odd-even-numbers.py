cnt=0
def comp(n):
    global cnt
    if n==1:
        print(cnt+1)
        return 0
    if n==2:
        print(cnt+2)
        return 0
    if n%2==1:
        cnt+=n
        
        comp(n-2)
    if n%2==0:
        cnt+=n
        comp(n-2)
n=int(input())
comp(n)