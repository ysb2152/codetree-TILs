n=int(input())
score=list(map(float,input().split()))
grade=sum(score)/len(score)
print(f"{grade:.1f}")
if grade>=4.0:
    print("Perfect")
elif grade>=3.0:
    print("Good")
else:
    print("Poor")