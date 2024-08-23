n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
new=[]
new=set(new)
for ele in b:
    if ele not in a:
        new.add(ele)

for ele in a:
    if ele not in b:
        new.add(ele)

print(len(new))