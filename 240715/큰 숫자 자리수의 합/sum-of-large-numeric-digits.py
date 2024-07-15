L=[]
cnt=0
def comp(n):
    if n<10:
        return n
    return comp(n//10)+n%10
a,b,c=map(int,input().split())
print(comp(a*b*c))