n=int(input())
class student:
    def __init__(self,h=0,w=0,n=0):
        self.h=h
        self.w=w
        self.n=n
L=[student() for _ in range(n)]
for i in range(n):
    h,w=map(int,input().split())
    L[i].h=h
    L[i].w=w
    L[i].n=i+1
L.sort(key=lambda x:(-x.h,-x.w,n))
for student in L:
    print(f"{student.h} {student.w} {student.n}")