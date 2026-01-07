def postfix():
            for per in stack:
                if ord(per) in range(97,123):
                    rs.append(per)
                elif per in["+","-"] :
                    while back!=[]:
                        rs.append(back.pop())
                    back.append(per)
                    #continue
                elif per in["*","/"]:
                    while back!=[]:
                        while back[-1] not in ["+","-"]:
                            rs.append(back.pop())
                    back.append(per)
                    #continue
            while back!=[]:
                rs.append(back.pop())
            return(rs)
while True:
    try:
        back=[]
        rs=[]
        stack=input().split()           
        print(*postfix(),end="")
    except EOFError:
        break