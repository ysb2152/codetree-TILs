n=int(input())
summ=0
for i in range(1,101):
    summ+=i
    if summ>=n:
        print(f"{i}")    
        break