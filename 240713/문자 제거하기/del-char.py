c=input()

for _ in range(len(c)-1):
    k=int(input())
    
    c=list(c)
    if k<len(c):
     c.pop(k)

    if k>len(c):
        c.pop(len(c)-1)

    c=''.join(c)
    print(c)