A=input()
B=input()
def chrs(A,B):
    if B in A:
        print(A.find(B))
    else:
        print("-1")
chrs(A,B)