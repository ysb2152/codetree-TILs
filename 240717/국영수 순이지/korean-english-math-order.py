n=int(input())
class student:
    def __init__(self,name=0,kor=0,eng=0,math=0):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
L=[student() for _ in range(n)]
for i in range(n):
    a,b,c,d=input().split()
    b=int(b)
    c=int(c)
    d=int(d)
    L[i].name=a
    L[i].kor=b
    L[i].eng=c
    L[i].math=d
L.sort(key=lambda x:(-x.kor,-x.eng,-x.math))
for student in L:
    print(f"{student.name} {student.kor} {student.eng} {student.math}")