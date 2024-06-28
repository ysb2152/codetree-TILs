a,b=map(int,input().split())
print(f"{a}",end=" ")
while a<b:
    if a%2==1:
        a*=2
        if a>b:
            break
        print(f"{a}",end=" ")    
    if a%2==0:
        a+=3
        if a>b:
            break
        print(f"{a}",end=" ")