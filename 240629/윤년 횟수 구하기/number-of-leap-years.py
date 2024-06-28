cnt=0
cnt1=0
n=int(input())
for i in range(1,n+1):
    if i%100==0 and i%400!=0:
        cnt1+=1
    elif i%4==0:
        cnt+=1

print(f"{cnt}")