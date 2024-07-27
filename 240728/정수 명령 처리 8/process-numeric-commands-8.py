class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.node_num=0
    def push_front(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head!=None:
            self.head.prev=new_node
            self.head=new_node
            new_node.prev=None
        else:
            self.head=new_node
            self.tail=new_node
            new_node.prev=None
        self.node_num+=1
    def push_back(self,new_data):
        new_node=Node(new_data)
        new_node.prev=self.tail
        if self.tail !=None:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=None
        else:
            self.head=new_node
            self.tail=new_node
            new_node.next=None
        self.node_num+=1
    def pop_front(self):
        if self.head==None:
            print("empty")
        elif self.head.next==None:
            sav=self.head
            self.head=None
            self.tail=None
            self.node_num=0
            return sav.data
        else:
            sav=self.head
            self.head.next.prev=None
            self.head=self.head.next
            sav.next=None
            self.node_num-=1
            return sav.data
    def pop_back(self):
        if self.tail==None:
            print("empty")
        elif self.tail.prev==None:
            sav=self.tail
            self.head=None
            self.tail=None
            self.node_num=0
            return sav.data
        else:
            sav=self.tail
            self.tail.prev.next=None
            self.tail=sav.prev
            sav.prev=None
            self.node_num-=1
            return sav.data
    def size(self):
        return self.node_num
    def empty(self):
        if self.node_num==0:
            return 1
        else:
            return 0
    def front(self):
        return self.head.data
    def back(self):
        return self.tail.data
n=int(input())
a=DoublyLinkedList()
for i in range(n):
    order=input()
    if order.startswith('push_front'):
        _,num=tuple(order.split())
        num=int(num)
        a.push_front(num)
    if order.startswith('push_back'):
        _,num=tuple(order.split())
        num=int(num)
        a.push_back(num)
    if order.startswith('pop_front'):
                
        print(a.pop_front())
    if order.startswith('pop_back'):
               
        print(a.pop_back())
    if order.startswith('size'):
       
        print(a.size())
    if order.startswith('empty'):
        
        print(a.empty())
    if order.startswith('front'):
        
        print(a.front())
    if order.startswith('back'):
        
        print(a.back())