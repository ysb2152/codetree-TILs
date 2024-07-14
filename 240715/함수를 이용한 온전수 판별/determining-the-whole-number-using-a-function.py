def div1(n):
    if n%3==0 and n%9!=0:
        return False
    else:
        return True
def number(n):
    if i%10!=5:
        return div1(n)
def div2(n):
    if n%2!=0:
        return number(n)
a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if div2(i)==True:
        
        cnt+=1
print(cnt)