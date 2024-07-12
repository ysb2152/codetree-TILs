c=input()
L=[]
for i in range(0,len(c)):
    if i%2==1:
        L.append(c[i])
L=L[::-1]
for ele in L:
    print(ele,end="")