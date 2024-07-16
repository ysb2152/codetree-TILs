n=int(input())
class student:
    def __init__(self,name=0,a=0,b=0,c=0):
        self.name=name
        self.a=a
        self.b=b
        self.c=c
L=[student() for _ in range(n)]
for i in range(n):
    a,b,c,d=input().split()
    b=int(b)
    c=int(c)
    d=int(d)
    L[i].name=a
    L[i].a=b
    L[i].b=c
    L[i].c=d
L.sort(key=lambda x: x.a+x.b+x.c)
for student in L:
    print(f"{student.name} {student.a} {student.b} {student.c}")