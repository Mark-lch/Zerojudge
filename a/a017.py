def Change():
    rs=[]
    tp=[]
    for per in data:
        if per not in ["+","-","*","/","(",")","%"]:
            rs.append(per)
        
        elif per=="(":
            tp.append(per)
        
        elif per==")":
            while tp and tp[-1]!="(":
                rs.append(tp.pop())
            else:
                tp.pop()

        elif per in ["+","-","*","/","%"]:
            while tp and per in ["+","-"] and tp[-1]!="(":
                rs.append(tp.pop())
            while tp and tp[-1] in ["*","/","%"] and per in ["*","/","%"] and tp[-1]!="(":
                rs.append(tp.pop())
            tp.append(per)

    while tp:
        rs.append(tp.pop())
    return(rs)


def Operation(value:list):
    RS=[]
    for per in value:
        if per not in ["+","-","*","/","%"]:
            RS.append(per)
        else:
            b=int(RS.pop())
            a=int(RS.pop())
            if per=="+":
                RS.append(a+b)
            elif per=="-":
                RS.append(a-b)
            elif per=="*":
                RS.append(a*b)
            elif per=="/":
                RS.append(a//b)
            else:
                RS.append(a%b)
    return(RS)           



while True:
    try:
        data=input().split()
        print(*Operation(Change()))
    except EOFError:
        break