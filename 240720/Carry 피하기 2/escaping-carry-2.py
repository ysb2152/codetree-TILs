n=int(input())
L=[int(input()) for _ in range(n)]
comb=[]
maximum=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            comb.append([L[i],L[j],L[k]])
for i in range(len(comb)):
    if comb[i][0]%10+comb[i][1]%10+comb[i][2]%10 <10:
        for j in range(0,2):
            if comb[i][j]<10:
                comb[i].sort()
                comb[i][1] = comb[i][0] + comb[i][1]
                comb[i][0]=0
                if comb[i][0]%100+comb[i][1]%100+comb[i][2]%100 <100:
                    for j in range(0,2):
                        if comb[i][j]<100:
                            comb[i].sort()
                            comb[i][1] = comb[i][0] + comb[i][1]
                            comb[i][0]=0
                            if comb[i][0]%1000+comb[i][1]%1000+comb[i][2]%1000 <1000:
                                for j in range(0,2):
                                    if comb[i][j]<1000:
                                        comb[i].sort()
                                        comb[i][1] = comb[i][0] + comb[i][1]
                                        comb[i][0]=0
                                        if comb[i][0]%10000+comb[i][1]%10000+comb[i][2]%10000 <10000:
                                            for j in range(0,2):
                                                if comb[i][j]<10000:
                                                    comb[i].sort()
                                                    comb[i][1] = comb[i][0] + comb[i][1]
                                                    comb[i][0]=0
                                            maximum.append(comb[i])
for i in range(len(maximum)):
    maximum[i]=sum(maximum[i])
if maximum=[]:
    print("-1")
else:
    print(max(maximum))