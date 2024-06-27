aa,ae=input().split()
ba,bs=input().split()
aa=int(aa)
ba=int(ba)
if (aa>=19 or ba>=19):
    if ae=='M' or bs=='M':
        print("1")
    else:
        print("0")
else:
    print("0")