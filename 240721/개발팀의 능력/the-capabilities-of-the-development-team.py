import sys
L=list(map(int,input().split()))

def diff(a,b,c,d):
	sum1=L[a]+L[b]
	sum2=L[c]+L[d]
	sum3=sum(L)-sum1-sum2
	min_val = min(sum1, sum2, sum3)
	max_val = max(sum1, sum2, sum3)

	calc = 0
	if(sum1 != sum2 and sum2!= sum3 and sum1 !=sum3):
		calc= max_val - min_val

	return calc

	
	
min_diff=sys.maxsize
for i in range(5):
	for j in range(i + 1, 5):
		for k in range(5):
			for l in range(k + 1, 5):
				if k == i or k == j or l == i or l == j:
					continue
				if diff(i,j,k,l)!=0:
					min_diff= min(min_diff,diff(i,j,k,l))
		  

print(min_diff)