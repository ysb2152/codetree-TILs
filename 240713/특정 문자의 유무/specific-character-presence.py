c=input()
a="No"
b="No"
for i in range(len(c)-1):
    if c[i:i+2]=='ee':
        a="Yes"
    
    if c[i:i+2]=='ab':
       b="Yes"
    
       
print(a,end=" ")
print(b)