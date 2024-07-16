class person:
    def __init__(self,name=0,height=0,weight=0):
        self.name=name
        self.height=height
        self.weight=weight
n=int(input())
L=[person() for _ in range(n)]
for i in range(n):
    a,b,c=tuple(input().split())
    L[i].name=a
    L[i].height=b
    L[i].weight=c
L.sort(key=lambda x: x.height)

for person in L:
    print(person.name,person.height,person.weight)