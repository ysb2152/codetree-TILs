c=input()
c=list(c)
c.pop(1)
c.pop(len(c)-2)
c=''.join(c)
print(c)