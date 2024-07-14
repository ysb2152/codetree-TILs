def plus(a,c):
    print(f"{a} + {c} = {a+c}")
def minus(a,c):
    print(f"{a} - {c} = {a-c}")
def mul(a,c):
    print(f"{a} * {c} = {a*c}")
def div(a,c):
    print(f"{a} / {c} = ({a/c}):.0f")
a,o,c=input().split()
a=int(a)
c=int(c)
if o=='+':
    plus(a,c)
elif o=='-':
    minus(a,c)
elif o=='*':
    mul(a,c)
elif o=='/':
    div(a,c)
else:
    print("False")