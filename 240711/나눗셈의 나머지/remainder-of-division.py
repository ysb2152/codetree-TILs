a,b=map(int,input().split())
L=[0 for _ in range (10)]
while a>1:
    L[a%b]+=1
    a=a//b
summ=0

for ele in L:
    summ=summ+ele**2
    

print(summ)