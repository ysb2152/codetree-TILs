class info:
    def __init__(self,code,color,second):
        self.code=code
        self.color=color
        self.second=second
c,co,se=tuple(input().split())
info1=info(c,co,se)
print(f"code : {info1.code}")
print(f"color : {info1.color}")
print(f"second : {info1.second}")