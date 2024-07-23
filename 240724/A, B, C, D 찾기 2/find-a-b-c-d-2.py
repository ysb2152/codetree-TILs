L=list(map(int,input().split()))
L.sort()


for A in range(1,max(L)):
    
    for B in range(1,max(L)):
        
        for C in range(1,max(L)):
            
            for D in range(1,max(L)):
                
                if (A+B in L) and (B+C in L) and (C+D in L) and (D+A in L) and (A+C in L) and (B+D in L) and (A+B+C in L) and (A+B+D in L) and (A+C+D in L) and (B+C+D in L) and (A+B+C+D) in L:
                    if A<=B and B<=C and C<=D:
                        T=[A,B,C,D]
                        if (T.count(A)<=L.count(A)) and (T.count(B)<=L.count(B)) and (T.count(C)<=L.count(C)) and (T.count(D)<=L.count(D)):
                            print(A,B,C,D)