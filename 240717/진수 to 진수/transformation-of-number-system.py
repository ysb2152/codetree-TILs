a,b=map(int,input().split())
n=input()
n=list(n)
L=[]
ans=[]
num=0
for i in range(len(n)):
    num=a*i+int(n[i])
while True:
    if num<b:
        ans.append(num)
        break
    ans.append(num%b)
    num//=b
for ele in ans:
    print(ele,end="")