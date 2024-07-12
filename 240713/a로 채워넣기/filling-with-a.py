c=input()
c=list(c)
c[1]='a'
c[len(c)-2]='a'
c=''.join(c)
print(c)