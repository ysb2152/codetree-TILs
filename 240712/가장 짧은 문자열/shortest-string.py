a=input()
b=input()
c=input()
L=[len(a),len(b),len(c)]
k=L.index(min(L))
p=L.index(max(L))
print(f"{L[p]-L[k]}")