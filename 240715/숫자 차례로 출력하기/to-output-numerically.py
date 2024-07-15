def line(n):
    if n==0:
        return
    line(n-1)
    print(n,end=" ")
def line2(n):
    
    if n==0:
        return
    
    print(n,end=" ")
    line2(n-1)
n=int(input())

line(n)
print(" ")
line2(n)