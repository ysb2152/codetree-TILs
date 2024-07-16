n=int(input())
class student:
    def __init__(self,height=0,weight=0,n=0):
        self.height=height
        self.weight=weight
        self.n=n
L=[student() for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    L[i].height=a
    L[i].weight=b
    L[i].n=i+1
L.sort(key=lambda x: (x.height,-x.weight))
for student in L:
    print(f"{student.height} {student.weight} {student.n}")