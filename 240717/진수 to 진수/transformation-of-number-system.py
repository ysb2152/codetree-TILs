a,b=map(int,input().split())
n=input()
n=list(n)

ans=[]
num=0
for i in range(len(n)):
    num=num*a+int(n[i])
while True:
    if num<b:
        ans.append(num)
        break
    ans.append(num%b)
    num//=b
ans=ans[::-1]
for ele in ans:
    print(ele,end="")