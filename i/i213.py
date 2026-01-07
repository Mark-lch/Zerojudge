N=int(input())
stack=[]
while N>0:
    k=list(map(int,input().split()))
    if k[0]==1:
        stack.append(k[1])

    elif k[0]==2:
        if stack:
            print(stack[-1])
        else:
            print("-1")
    else:
        if stack:
            stack.pop()
    N-=1