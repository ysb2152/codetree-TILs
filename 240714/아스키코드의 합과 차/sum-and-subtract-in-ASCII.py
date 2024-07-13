L=list(input().split())
a=L[0]
b=L[1]
print(ord(a)+ord(b),end=" ")
if ord(a)>ord(b):
    print(ord(a)-ord(b))
elif ord(a)<ord(b):
    print(ord(b)-ord(a))
else:
    print("0")