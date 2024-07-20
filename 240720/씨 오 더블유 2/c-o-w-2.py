n=int(input())
L=input()
L=list(L)
c,o,w=0,0,0
for i in range(n):
	if L[i]=='C':
		c+=1
	if L[i]=='O':
		o+=1
	if L[i]=='W':
		w+=1
print(c*o*w)