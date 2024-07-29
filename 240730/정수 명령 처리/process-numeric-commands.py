n=int(input())
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
for _ in range(n):
    a=input()
    
    if a.startswith('push'):
        b,c=tuple(a.split())
        c=int(c)
        Stack.push(c)
    if a.startswith('pop'):
        print(Stack.pop())
    if a.startswith('size'):
        print(Stack.size())
    if a.startswith('empty'):
        if Stack.empty():
            print("1")
        else:
            print("0")
    if a.startswith('top'):
        print(Stack.top())