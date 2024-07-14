def pal(A):
    A=list(A)
    if A==A[::-1]:
        print("Yes")
    else:
        print("No")
A=input()
pal(A)