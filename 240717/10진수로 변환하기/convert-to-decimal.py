a=int(input())
L=[]
for i in range(0,5):
    L.append(a%10)
    a//=10
L=L[::-1]
num=0
for i in range(len(L)):
    num=num*2+L[i]
print(num)