class person:
    def __init__(self,name=0,height=0,weight=0):
        self.name=name
        self.height=height
        self.weight=weight
L=[person() for _ in range(5)]
for i in range(5):
    a,b,c=input().split()
    b=int(b)
    c=float(c)
    L[i].name=a
    L[i].height=b
    L[i].weight=c
L.sort(key=lambda x:(x.name))
print("name")
for person in L:
    print(f"{person.name} {person.height} {person.weight}")
L.sort(key=lambda x:(-x.height))
print(" ")
print("height")
for person in L:
    print(f"{person.name} {person.height} {person.weight}")