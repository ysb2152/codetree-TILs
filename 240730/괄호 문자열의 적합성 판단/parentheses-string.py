class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def pop(self):
        if self.empty():
            return Exception("Stack is empty")
        return self.items.pop()
    def top(self):
        if self.empty():
            return Exception("Stack is empty")
        return self.items[-1]
Stack=stack()
def solution(a):
  s = stack()
  for i in range(len(a)): 
    if a[i] == '(':          
      s.push('(')            
    else:
      if s.empty() == True:   
        return False          
      s.pop()                 

  if s.empty() == False:      
    return False              
  return True         
a=input()
if solution(a):
    print("Yes")
else:
    print("No")