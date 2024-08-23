n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

new=[]
new=set(new)
for ele in b:
    if ele not in a and ele not in new:
        new.add(ele)

for ele in a:
    if ele not in b and ele not in new:
        new.add(ele)

print(len(new))