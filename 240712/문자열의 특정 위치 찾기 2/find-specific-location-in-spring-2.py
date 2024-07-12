L=["apple","banana","grape","blueberry","orange"]
c=input()
cnt=0
p=[]
for j in range(0,5):
    for i in range(0,len(L[j])):
        if L[j][2]==c or L[j][3]==c:
            cnt+=1
            print(L[j])
            break

print(cnt)