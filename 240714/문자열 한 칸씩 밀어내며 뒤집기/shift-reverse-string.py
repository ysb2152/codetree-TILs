c,q=input().split()
q=int(q)
for _ in range(q):
    i=int(input())
    if i==1:
        c=c[1:]+c[0]
        print(c)
    if i==2:
        c=c[len(c)-1]+c[:len(c)-1]
        print(c)
    if i==3:
        c=c[::-1]
        print(c)