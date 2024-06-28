n=int(input())
summ=0
for i in range(1,101):
    if summ>=n:
        summ-=(i-1)
        break
    if summ==1:
        break
    summ+=i
print(f"{summ}")