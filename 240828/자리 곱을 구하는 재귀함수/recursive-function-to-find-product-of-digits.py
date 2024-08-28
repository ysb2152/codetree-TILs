a,b,c=map(int,input().split())
ans=a*b*c
#print(ans)
real=1
def cal(a):
    global ans
    global real
    if a<10:
        real*=a
        return real
    if ans%10!=0:
        real*=ans%10
    ans=int(ans//10)
    cal(ans)

cal(ans)
print(real)