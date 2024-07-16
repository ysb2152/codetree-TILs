class agent:
    def __init__ (self,codename=0,score=0):
        self.codename=codename
        self.score=score
L=[agent() for _ in range(5) ]
for i in range(5):
    a,b=tuple(input().split())
    L[i]=agent(a,b)
P=[]
for i in range(5):
    P.append(int(L[i].score))
print(L[P.index(min(P))].codename,end=" ")
print(L[P.index(min(P))].score,end=" ")