cnt=0
def comp(n):
    global cnt
    if n<10:
        cnt+=(n%10)**2
        return n
    cnt+=(n%10)**2
    return comp((n//10))+(n%10)
n=int(input())
comp(n)
print(cnt)