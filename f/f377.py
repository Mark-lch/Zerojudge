def postfix():
    tem=[]
    rs=[]
    for per in stack:
        if per.isalpha():
            rs.append(per)
        
        elif per =="(":
            tem.append(per)
            
        elif per ==")":
            while tem[-1]!="(":
                rs.append(tem.pop())
            else:
                tem.pop()
        elif per in["+","-","*","/"] :

            while per in ["+","-"] and tem and (tem[-1]!="(") :
                rs.append(tem.pop()) #+ -

            while tem and (tem[-1] not in ["+","-","("]) and per in ["/","*"]: 
                rs.append(tem.pop()) #* /

            tem.append(per)

    while tem:
        rs.append(tem.pop())

    return(rs)

while True:
    try:
        stack=input().split()           
        print(*postfix(),sep=" ")
    except EOFError:
        break