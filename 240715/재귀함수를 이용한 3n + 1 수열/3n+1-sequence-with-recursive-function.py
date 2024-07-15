cnt=0
def comp(n):
    global cnt
    if n==1:
        return cnt
    if n%2==0:
        cnt+=1
        return comp(n//2)
    if n%2==1:
        cnt+=1
        return comp(n*3+1)
n=int(input())
print(comp(n))