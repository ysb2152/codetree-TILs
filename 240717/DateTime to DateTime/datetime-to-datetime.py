a,b,c=map(int,input().split())
mini=0
a1=11
b1=11
c1=11
def tim(a,b,c):
    global mini
    global a1
    global b1
    global c1
    if a1>a:
        return -1
    elif b1>b:
        return -1
    elif c1>c:
        return -1
    while True:
        if a1==a and b1==b and c1==c:
            return mini
            
        c1+=1
        mini+=1
        if c1==60:
            b1+=1
            c1=0
        if b1==24:
            a1+=1
            b1=0
    
print(tim(a,b,c))