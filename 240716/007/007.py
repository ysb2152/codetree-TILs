code,place,time=input().split()
class no:
    def __init__(A,code,place,time):
        A.code=code
        A.place=place
        A.time=time
A1=no(code,place,time)
print(f"secret code : {A1.code}")
print(f"meeting point : {A1.place}")
print(f"time : {A1.time} ")