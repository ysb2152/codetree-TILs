n=int(input())
class person:
    def __init__(self,name=0,height=0,weight=0):
        self.name=name
        self.height=height
        self.weight=weight
L=[person() for _ in range(n)]
for i in range(n):
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    L[i].name=a
    L[i].height=b
    L[i].weight=c
L.sort(key=lambda x:(x.height,-x.weight))
for person in L:
    print(f"{person.name} {person.height} {person.weight}")