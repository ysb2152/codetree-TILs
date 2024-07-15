n,k,t=input().split()
n=int(n)
k=int(k)
p=[]
for _ in range(n):
    a=input()
    if t in a:
        if a.find(t)==0:
            p.append(a)
p.sort()
print(p[k-1])