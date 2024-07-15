cnt=0
def comp(n):
    global cnt
    if n==0:
        return 
       
    cnt+=n
    
    comp(n-1)
    
n=int(input())
comp(n)
print(cnt)