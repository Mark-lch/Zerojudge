a,b=map(int,input().split())
Result=[]
for digital in range(a,b+1):
    total=0
    sd=str(digital)
    for per in sd:
        total+=int(per)**len(sd)
    if digital==total: Result.append(digital)
if Result:
    print(*Result)
else:
    print("none")