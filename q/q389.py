while True:
    try:
        N=int(input())
        
        count=0

        if N==0:
            P=1
        elif N>0:
            N+=1
            P=abs(N)
        else:
            P=abs(N)
        
        for A in (range(10000)if N>=0 else range(-1,-10000,-1)):
            live=False
            Year=(4499+A)**2
            M=int(str(Year)[-4:-2])
            Z=int(str(Year)[-2:])
            if M<1 or M>12:
                continue
            elif M==2 and 1<=Z<=28:
                live=True
            elif M in [1, 3, 5, 7, 8, 10, 12] and 1<=Z<=31:
                live=True
            elif M in [4, 6, 9, 11] and 1<=Z<=30:
                live=True
            else:
                continue
            
            if live:
                count+=1
            
            if count==P:
                print(Year)
                break
    except EOFError:
        break
        
"""舊的寫法，沒用for，又臭又長，還有迴圈限制1000次。以後不亂寫了，凡事先用for總沒錯:)"""
        #def Daycheck(N):
        #    count=0
        #    global live,P
        #    Year=(4499+N)**2
        #    M=int(str(Year)[-4:-2])
        #    Z=int(str(Year)[-2:])
        #
        #    if M<1 or M>12:
        #        if N>0:
        #            return Daycheck(N+1)
        #        else:
        #            return Daycheck(N-1)
        #    if M==2 and 1<=Z<=28:
        #        live=True
        #    elif M in [1, 3, 5, 7, 8, 10, 12] and 1<=Z<=31:
        #        live=True
        #    elif M in [4, 6, 9, 11] and 1<=Z<=30:
        #        live=True
        #    else:
        #        if N>0:
        #            return Daycheck(N+1)
        #        else:
        #            return Daycheck(N-1)
        #    
        #    if live:
        #        count+=1
        #        if N>0:
        #            return Daycheck(N+1)
        #        else:
        #            return Daycheck(N-1)
        #    if count==P:
        #        print(Year)
        #        return(Year)
                
        #Daycheck(N)