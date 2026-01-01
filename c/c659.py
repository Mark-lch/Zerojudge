while True:
    try:
        rs=input().split()
        sp=rs.pop(0)
        #print(rs)
        print(*rs,sep=f" {sp} ")
    except EOFError:
        break