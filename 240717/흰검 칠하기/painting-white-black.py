n=int(input())
L=[0 for _ in range(10000)]
Gray=[0 for _ in range(10000)]
curr=0
point=[]
offset=5000
for _ in range(n):
	x,direction=tuple(input().split())
	x=int(x)
	if direction=='L':
		left=curr-x
		right=curr
		curr-=x
		left+=offset
		right+=offset
		for i in range(left,right):
			L[i]='W'		       
	else:
		left=curr
		right=curr+x
		curr+=x
		left+=offset
		right+=offset
		for i in range(left,right):
			L[i]='B'	
	point.append([left,right])
for left,right in point:
	for i in range(left,right):
		Gray[i]+=1
Graycnt=0
Blackcnt=0
Whitecnt=0

for i in range(len(Gray)):
	if Gray[i]>=4:
		L[i]='G'
for ele in L:
	if ele=='B':
		Blackcnt+=1
	if ele=='G':
		Graycnt+=1
	if ele=='W':
		Whitecnt+=1
print(Whitecnt,Blackcnt,Graycnt)