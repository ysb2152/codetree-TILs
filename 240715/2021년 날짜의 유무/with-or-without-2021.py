def isdate(a,b):
    if a>=13:
        return False
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        if b<=31:
            return True
        else:
            return False
    elif a==2:
        if b<=28:
            return True
        else:
            return False
    else:
        if b<=30:
            return True
        else:
            return False
M,D=map(int,input().split())
if isdate(M,D)==True:
    print("Yes")
else:
    print("No")