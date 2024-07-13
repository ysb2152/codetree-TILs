c=input()
if 'e' in c:
    c=c[:c.find('e')]+c[(c.find('e'))+1:]
print(c)