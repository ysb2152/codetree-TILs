a,b=input().split()
for ele in a:
    if ele.isdigit()==False:
        a=a[:a.find(ele)]
for ele in b:
    if ele.isdigit()==False:
        b=b[:b.find(ele)]
print(int(a)+int(b))