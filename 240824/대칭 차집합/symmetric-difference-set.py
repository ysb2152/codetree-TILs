n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

new=[]
new=set(new)
for ele in b:
    if ele in a:
        new.add(ele)


print(n+m-(2*len(new)))