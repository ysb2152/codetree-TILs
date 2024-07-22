x,y=map(int,input().split())
cnt = 0
max_num=0
for i in range(x, y+1):
    if i<10:
        max_num=max(max_num,i)
    if 10<=i and i<100:
        d1=i//10
        d2=i%10
        max_num=max(max_num,d1+d2)
    if 100<=i and i<1000:
        d1=i//100
        d2=(i-d1)//10
        d3=(i-d1)%10
        max_num=max(max_num,d1+d2+d3)
    if i<=1000 and i<10000:
        d1=i//1000
        d2=(i-d1)//100
        d3=(i-d1-d2)//10
        d4=(i-d1-d2)%10
        max_num=max(max_num,d1+d2+d3+d4)

        
   

print(max_num)