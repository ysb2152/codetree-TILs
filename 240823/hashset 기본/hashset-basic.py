n=int(input())
s=set()
for _ in range(n):
    a=input()
    if a.startswith('add'):
        _,x=a.split()
        s.add(x)
    if a.startswith('remove'):
        _,x=a.split()
        s.remove(x)
    if a.startswith('find'):
        _,x=a.split()
        if x in s:
            print("true")
        else:
            print("false")