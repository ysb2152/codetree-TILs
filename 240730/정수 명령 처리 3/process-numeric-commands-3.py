from collections import deque
dq=deque()
n=int(input())
for _ in range(n):
    order=input()
    if order.startswith('push_front'):
        a,b=tuple(order.split())
        dq.appendleft(b)
    if order.startswith('push_back'):
        a,b=tuple(order.split())
        dq.append(b)
    if order.startswith('pop_front'):
        print(dq.popleft())
    if order.startswith('pop_back'):
        print(dq.pop())
    if order.startswith('size'):
        print(len(dq))
    if order.startswith('empty'):
        if dq:
            print("0")
        else:
            print("1")
    if order.startswith('front'):
        print(dq[0])
    if order.startswith('back'):
        print(dq[-1])