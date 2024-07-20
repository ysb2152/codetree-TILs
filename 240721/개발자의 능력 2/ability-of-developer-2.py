import sys
L=list(map(int,input().split()))
L.sort()
def summ(a,b):
    sum1=L[a]+L[b]
    sum2=L[0]+L[len(L)-1]
    sum3=sum(L)-sum1-sum2
    
    return (abs(max(sum1,sum2,sum3)-min(sum1,sum2,sum3)))
mini=sys.maxsize
for i in range(1,5):
    for j in range(i+1,5):
        mini=min(mini,summ(i,j))
print(mini)