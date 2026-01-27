def atc(n,fm,tem,t):
    
    if n==0:
        return
    
    atc(n-1,fm,t,tem)

    print(f"Move disc {n} from {fm} to {t}")
    
    atc(n-1,tem,fm,t)

N=int(input())
atc(N,"A","B","C")



"""2"""
# 1 a to b
# 2 a to c
# 1 b to c 

"""3"""
# 1 a to c
# 2 a to b
# 1 c to b
# 3 a to c
# 1 b to a
# 2 b to c
# 1 a to c
# :7times 1:4 2:2 3:1