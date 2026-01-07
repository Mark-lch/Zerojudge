while True:
    try:
        wide,M,time=int(input()),input(),int(input())
        #result=[]
        #for a in range(time):
        #    if a<len(M) :
        #        result.append(M[a])
        #    if (time>wide and len(result)>wide) or a>len(M):
        #        result.pop(0)
        #print(*result,sep="")
        
        #Start=time
        #if Start<0:
        #    Start=0
        M=" "*wide+M+" "*wide
        print(M[time:time+wide])
    except EOFError:
        break