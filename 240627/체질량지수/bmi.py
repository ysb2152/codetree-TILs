h,w= map(int,input().split())

b=int(w//((h/100)**2))
print(f"{b}")
if b>=25:
    print("Obesity")