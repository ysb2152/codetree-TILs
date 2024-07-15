def hello(n):
    if n==0:
        return
    hello(n-1)
    print("HelloWorld")
N=int(input())
hello(N)