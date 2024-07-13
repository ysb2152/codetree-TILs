a=input()
b=input()
a1=[]
b1=[]
for ele in a:
    if ele.isdigit()==True:
        a1.append(ele)
for ele in b:
    if ele.isdigit()==True:
        b1.append(ele)

a=''.join(a1)
b=''.join(b1)

print(int(a)+int(b))