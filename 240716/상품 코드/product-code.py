class prod:
    def __init__(self,name=0,code=0):
        self.name=name
        self.code=code
L=[prod() for _ in range(2)]
L[0].name="codetree"
L[0].code="50"
n,c=tuple(input().split())
L[1].name=n
L[1].code=c
print(f"product {L[0].code} is {L[0].name }")
print(f"product {L[1].code} is {L[1].name }")