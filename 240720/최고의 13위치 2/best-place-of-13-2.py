n=int(input())
L=[list(map(int,input().split())) for _ in range(n)]
cnt=0
for i in range(n):
	for j in range(n-2):
		for k in range(n):
			if k==i and n<6:
				continue

			
			for l in range(n-2):
				if k==i and j>n-6:
					continue
				cnt=max(cnt,L[i][j]+L[i][j+1]+L[i][j+2]+L[k][l]+L[k][l+1]+L[k][l+2])
print(cnt)