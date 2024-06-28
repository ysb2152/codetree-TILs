n=int(input())
c=0
f=0
t=0
for i in range(1,n+1):
    if i%12==0 :
        t+=1
    elif i%6==0 :
        f+=1
    elif i%2==0 :
        c+=1
    elif i%3==0:
        f+=1
print(f"{c}",end=" ")
print(f"{f}",end=" ")
print(f"{t}",end=" ")