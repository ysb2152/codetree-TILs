n=int(input())
L=[]
while True:
    if n<2:
        L.append(n)
        break
    L.append(n%2)
    n//=2
L=L[::-1]
for ele in L:
    print(ele,end="")