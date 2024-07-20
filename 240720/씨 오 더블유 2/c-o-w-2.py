n=int(input())
L=input()
L=list(L)
c,o,w=0,0,0
cnt=0
for i in range(n):
	o=0
	w=0
	if L[i]=='C':
		for j in range(i+1,n):
			if L[j]=='O':
				o+=1
			if L[j]!='O':
				continue
			
			for k in range(j+1,n):
				if L[k]=='W':
					w+=1
			cnt+=w*o
			w=0
			o=0
			
	
print(cnt)