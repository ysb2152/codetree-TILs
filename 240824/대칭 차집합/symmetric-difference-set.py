n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


new=set(a)
for ele in b:
    if ele not in new:
        new.add(ele)
new1=set(b)
for ele in a:
    if ele not in new1:
        new1.add(ele)
print(len(new)-n+len(new1)-m)