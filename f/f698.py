lst=input().split()
stack=[]
for per in lst:
    if per.isalnum():
        stack.append(per)
    else:
        n2=int(stack.pop())
        n1=int(stack.pop())
        if per=="-":
            stack.append(n1-n2)
        elif per=="+":
            stack.append(n1+n2)
        elif per=="*":
            stack.append(n1*n2)
        else:
            stack.append(n1//n2)
    
    print(n2,per,n1)