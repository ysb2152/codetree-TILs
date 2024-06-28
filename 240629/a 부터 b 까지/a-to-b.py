a,b=map(int,input().split())
print(f"{a}",end=" ")
while a<b:
 if a%2==1:
        a*=2
        print(f"{a}",end=" ")    
 if a%2==0:
        a+=3
        print(f"{a}",end=" ")