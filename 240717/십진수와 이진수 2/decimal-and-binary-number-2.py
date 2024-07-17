n=input()
n=list(n)
num=0
for i in range(len(n)):
    num=num*2+int(n[i])
num*=17
L=[]
while True:
    if num<2:
        L.append(num)
        break
    L.append(num%2)
    num//=2
L=L[::-1]
for ele in L:
    print(ele,end="")