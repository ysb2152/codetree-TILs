a=0
b=0
for i in range(10):
    i=int(input())
    if i%3==0:
        a+=1
    if i%5==0:
        b+=1
print(f"{a}",end=" ")
print(f"{b}",end=" ")