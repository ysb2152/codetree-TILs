a,b,c=map(int,input().split())
mini=0
a1=11
b1=11
c1=11
while True:
    if a1==a and b1==b and c1==c:
        break
    c1+=1
    mini+=1
    if c1==60:
        b1+=1
        c1=0
    if b1==24:
        a1+=1
        b1=0
    
print(mini)