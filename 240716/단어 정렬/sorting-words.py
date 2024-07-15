n=int(input())
L=[]
for _ in range(n):
    a=input()
    L.append(a)
L.sort()
for ele in L:
    print(ele)