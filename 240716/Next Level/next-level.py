i,levels=input().split()
class form:
    def __init__(self,ids,level):
        self.ids=ids
        self.level=level
form1=form("codetree","10")
form2=form(i,levels)
print(f"user {form1.ids} lv {form1.level}")
print(f"user {form2.ids} lv {form2.level}")