c=input()
L=len(c)
for _ in range(L+1):
    print(c)
    k=c[L-1]+c[:L-1]
    c=k