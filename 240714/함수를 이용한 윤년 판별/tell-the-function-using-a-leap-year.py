def year(n):
    if (n%100)==0 and (n%400)!=0:
        return False
    if n%4==0:
        return True
y=int(input())
if year(y)==True:
    print("true")
else:
    print("false")