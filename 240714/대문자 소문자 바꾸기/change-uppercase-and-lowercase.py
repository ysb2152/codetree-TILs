c=input()
c=list(c)
for ele in c:
    if ord(ele)<97:
        print(ele.lower(),end="")
    if ord(ele)>=97:
        print(ele.upper(),end="")