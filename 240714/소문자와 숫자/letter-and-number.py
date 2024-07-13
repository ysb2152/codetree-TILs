c=input()
c=list(c)
for ele in c:
    if ele.isalpha()==True:
        print(ele.lower(),end="")
    elif ele.isdigit()==True:
        print(ele,end="")