import sys
def Count():
    club={}
    data=sys.stdin.read().split()

    it=iter(data)
    next(it)
    n=int(next(it))

    for _ in range(n):
        club.setdefault(next(it),0)

    start=2+n
    while start<len(data):
        tp=set()
        #for a in data[start:start+3]:
        tp.update(data[start:start+3])
        
        for b in tp:
            club[b]+=1
        start+=3
        
    
    for k,v in club.items():
        print(k,v)
Count()