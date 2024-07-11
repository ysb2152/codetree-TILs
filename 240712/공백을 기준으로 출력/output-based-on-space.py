a=input()
b=input()
a=list(a)
b=list(b)
for _ in range(len(a)):
    for ele in a:
        if ele==' ':
            a.remove(ele)
for _ in range(len(b)):
    for ele in b:
        if ele==' ':
            b.remove(ele)
for ele in a:
    print(ele,end="")
for ele in b:
    print(ele,end="")