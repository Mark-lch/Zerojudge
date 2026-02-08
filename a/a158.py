def GCD(a,b):
    if not b: return a
    return GCD(b,a%b)

input()
while True:
    try:
        data=list(map(int,input().split()))
        if not len(data): continue
        result=0
        temp=0
        for a in range(len(data)-1):
            for b in range(a+1,len(data)):
                temp=GCD(data[a],data[b])
                result=max(result,temp)
        print(result)

    except EOFError:
        break