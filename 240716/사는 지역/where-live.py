class info:
    def __init__(self,name=0,num=0,place=0):
        self.name=name
        self.num=num
        self.place=place
n=int(input())
L=[info() for _ in range(n)]
for i in range(n):
    name,num,place=tuple(input().split())
    L[i].name=name
    L[i].num=num
    L[i].place=place
p=[]
for i in range(n):
    p.append(L[i].name)
p.sort(reverse=True)
for i in range(n):
    if L[i].name==p[0]:
        print(f"name {L[i].name}")
        print(f"addr {L[i].num}")
        print(f"city {L[i].place}")