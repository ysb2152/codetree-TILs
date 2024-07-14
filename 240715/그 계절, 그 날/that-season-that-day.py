def isseason(M):
    if M>=3 and M<=5:
        print("Spring")
    if M>=6 and M<=8:
        print("Summer")
    if M>=9 and M<=11:
        print("Fall")
    if M==12 or (1<=M and M<=2):
        print("Winter")
def isdate(M,D):
    if M>=13:
        return False
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        if D<=31:
            return isseason(M)
        else:
            return False
    elif M==2:
        if D<=28:
            return isseason(M)
        else:
            return False
    else:
        if D<=30:
            return isseason(M)
        else:
            return False
def is4date(M,D):
    if M>=13:
        return False
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        if D<=31:
            return isseason(M)
        else:
            return False
    elif M==2:
        if D<=29:
            return isseason(M)
        else:
            return False
    else:
        if D<=30:
            return isseason(M)
        else:
            return False
def isyear(Y):
    if Y%4==0 and Y%100==0 and Y%400==0:
        return is4date(M,D)
    if Y%4==0 and Y%100!=0:
        return is4date(M,D)
    else:
        return isdate(M,D)
Y,M,D=map(int,input().split())
if isyear(Y)==False:
    print("-1")