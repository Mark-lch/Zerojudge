def process():
    RS=[]
    for per in lst:
        if per not in ["+","-","*","/"]:
            RS.append(per)
        else:
            n2=int(RS.pop())
            n1=int(RS.pop())
            if per=="-":
                RS.append(n1-n2)
            elif per=="+":
                RS.append(n1+n2)
            elif per=="*":
                RS.append(n1*n2)
            else:
                RS.append(n1//n2)
    return(RS)

while True:
    try:
        lst=input().split()
        print(*process())
    except EOFError:
        break