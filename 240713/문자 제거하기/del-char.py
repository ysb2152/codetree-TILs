c=input()

while len(c)>1:
    k=int(input())
    
    c=list(c)
    if k<len(c):
     c.pop(k)
    
    else:
        c.pop(len(c)-1)

    c=''.join(c)
    print(c)