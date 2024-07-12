c=input()
c=list(c)
a=c[1]
for i in range(len(c)):
    if a in c:
        c[c.index(a)]=c[0]
    if a not in c:    
        c=''.join(c)
        print(c)
        break