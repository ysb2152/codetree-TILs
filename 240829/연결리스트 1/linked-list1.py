class Node:
    def __init__(self, data):
        self.data = data # Linked list의 노드에 담을 데이터
        self.prev = None       # 초기에는 이전 노드와 다음 노드가 존재하지 않는다.
        self.next = None
# 노드 u 뒤에 단일 노드 singleton를 삽입
def insert_next(u, singleton):
    # singleton의 prev와 next를 설정
    singleton.prev = u
    singleton.next = u.next

    # singleton의 이전 노드의 next와
    # 다음 노드의 prev를 설정       
    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton
def insert_prev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u
    
    # singleton의 이전 노드의 next와
    # 다음 노드의 prev를 설정
    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton



S_init=input()
n=int(input())
cur=Node(S_init)
for _ in range(n):
    order=input()
    if order.startswith("1"):
        _,S_value=order.split()
        new_node=Node(S_value)
        insert_prev(cur,new_node)
        if cur.prev==None:
            print("(Null)",end=" ")
        else:
            print(cur.prev.data,end=" ")
        if cur==None:
            print("(Null)",end=" ")
        else:
            print(cur.data,end=" ")
        if cur.next==None:
            print("(Null)",end=" ")
        else:
            print(cur.next.data,end=" ")
        print(" ")
    if order.startswith("2"):
        _,S_value=order.split()
        new_node=Node(S_value)
        insert_next(cur,new_node)
        if cur.prev==None:
            print("(Null)",end=" ")
        else:
            print(cur.prev.data,end=" ")
        if cur==None:
            print("(Null)",end=" ")
        else:
            print(cur.data,end=" ")
        if cur.next==None:
            print("(Null)",end=" ")
        else:
            print(cur.next.data,end=" ")
        print(" ")
    if order.startswith("3"):
        if cur.prev!=None:
            cur=cur.prev
        if cur.prev==None:
            print("(Null)",end=" ")
        else:
            print(cur.prev.data,end=" ")
        if cur==None:
            print("(Null)",end=" ")
        else:
            print(cur.data,end=" ")
        if cur.next==None:
            print("(Null)",end=" ")
        else:
            print(cur.next.data,end=" ")
        print(" ")
    if order.startswith("4"):
        if cur.next!=None:
            cur=cur.next
        if cur.prev==None:
            print("(Null)",end=" ")
        else:
            print(cur.prev.data,end=" ")
        if cur==None:
            print("(Null)",end=" ")
        else:
            print(cur.data,end=" ")
        if cur.next==None:
            print("(Null)",end=" ")
        else:
            print(cur.next.data,end=" ")
        print(" ")