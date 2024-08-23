n=int(input())
a=list(map(int,input().split()))
a=set(a)
m=int(input())
b=list(map(int,input().split()))
for ele in b:
    if ele not in a:
        print("0")
    else:
        print("1")