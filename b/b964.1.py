input()
data=list(map(int,input().split()))
data.sort()
print(*data)
lower=[]
higher=[]
for a in data:
    if a<60:
        lower.append(a)
    else:
        higher.append(a)

if lower:
    print(lower[-1])
else:
    print("best case")

if higher:
    print(higher[0])
else:
    print("worst case")