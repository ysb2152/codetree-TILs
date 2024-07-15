cnt=0
def comp(n):
    global cnt
    if n==1:
        
        return 0
    if n%2==0:
        cnt+=1
        
        comp(n//2)
    else:
        cnt+=1
        
        comp(n//3)
n=int(input())
comp(n)
print(cnt)