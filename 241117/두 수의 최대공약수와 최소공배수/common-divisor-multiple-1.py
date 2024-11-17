a,b=map(int,input().split())
if a<b:
    big=b
    small=a
if b<a:
    big=a
    small=b
while small!=0:
    r=big%small
    big=small
    small=r
if a==b:    
    print(a,a)


else:
    print(big,int((a*b)/big))