total=0
for _ in range(5):
    data=list(map(int,input().split()))
    Max=max(data)
    if sum(data)-Max>Max: total+=1
print(total)