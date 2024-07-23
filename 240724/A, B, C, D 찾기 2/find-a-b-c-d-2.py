L=list(map(int,input().split()))
L.sort()
summ=sum(L)

for A in range(1,max(L)+1):
    for B in range(1,max(L)+1):
        for C in range(1,max(L)+1):
            for D in range(1,max(L)+1):
                if (A in L) and (B in L) and (C in L) and (D in L):
                    if (A+B in L) and (B+C in L) and (C+D in L) and (D+A in L) and (A+C in L) and (B+D in L):
                        if (A+B+C in L) and (A+B+D in L) and (A+C+D in L) and (B+C+D in L):
                            if (A+B+C+D) in L:
                                if A<=B and B<=C and C<=D:
                                    print(A,B,C,D)