n=int(input())
L=[input() for _ in range(n)]
c=input()
cnt=0
cnt1=0
for i in range(0,len(L)):
    if L[i][0]==c:
        cnt+=1
        cnt1+=len(L[i])
print(cnt,end=" ")
print(f"{(cnt1/cnt):.2f}")