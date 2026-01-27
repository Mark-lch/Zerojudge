A=input().split()
fact=input().split()
lack,surplus=0,0
for _ in range(int(A[-1])):
    order=input().split()
    for X in order[1:]:
        try:
            fact.remove(X)
        except ValueError:
            lack+=1
            continue
surplus=len(fact)

print(lack,surplus)    