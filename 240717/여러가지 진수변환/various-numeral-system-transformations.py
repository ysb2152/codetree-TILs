n,b=map(int,input().split())
L=[]
while True:
    if n<b:
        L.append(n)
        break
    L.append(n%b)
    n=n//b
L=L[::-1]
for ele in L:
    print(ele,end="")