n=int(input())
class data:
    def __init__(self,date=0,week=0,weather=0):
        self.date=date
        self.week=week
        self.weather=weather
L=[data() for _ in range(n)]
for i in range(n):
    a,b,c=input().split()
    L[i].date=a
    L[i].week=b
    L[i].weather=c
p=[]
for i in range(n):
    if L[i].weather=="Rain":
        p.append(L[i])
rain=[]
for i in range(len(p)):
    rain.append(p[i].date)
rain.sort()
for i in range(n):
    if L[i].date==rain[0] and L[i].weather=="Rain":
        print(f"{L[i].date} {L[i].week} {L[i].weather} ")