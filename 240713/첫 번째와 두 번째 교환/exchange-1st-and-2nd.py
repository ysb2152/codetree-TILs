a=input()
a=list(a)
b=[]
for i in range(0,len(a)):
    if a[i]==a[0]:
        b.append(a[1])
    elif a[i]==a[1]:
        b.append(a[0])
    else:
        b.append(a[i])
b=''.join(b)
print(b)