n=int(input())
class even:
    def __init__(self,num=0,t=0):
        self.num=num
        self.t=t
L=[even() for _ in range(n)]
k=list(map(int,input().split()))
for i in range(n):
    a=k[i]
    L[i].num=a
    L[i].t=i+1

L.sort(key=lambda x:(x.num,x.t))
t=[]
for i in range(n):
    for j in range(n):
        if k[i]==L[j].num:
            t.append(j+1)
            L[j].num=0
            break
for ele in t:
    print(ele,end=" ")