L=[input() for _ in range(10)]
c=input()

cnt=0
for i in range(0,len(L)):
    if L[i][len(L[i])-1]==c:
        print(L[i])
        cnt+=1
if cnt==0:
    print("None")