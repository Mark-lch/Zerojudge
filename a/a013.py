import sys
def calculate():
    data=sys.stdin.read().split()
    it=iter(data)
    Result=[]
    dic = {"M":1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1} 
    while True:
        try:
            A=next(it)
            B=next(it)
            if A==B:
                Result.append("ZERO")
                continue
            alpha=0
            beta=0
            skip=False
            for a in range(len(A)-1,-1,-1):
                if skip:
                    skip=False
                    continue
                elif a>0:
                    if dic.get(A[a])>dic.get(A[a-1]):
                        alpha+=dic.get(A[a-1:a+1])
                        skip=True
                    else:alpha+=dic.get(A[a])
                    
                else:alpha+=dic.get(A[a])
            skip=False
            for b in range(len(B)-1,-1,-1):
                if skip:
                    skip=False
                    continue
                if b>0:
                    if dic.get(B[b])>dic.get(B[b-1]):
                        beta+=dic.get(B[b-1:b+1])
                        skip=True
                    else:beta+=dic.get(B[b])
                    
                else:beta+=dic.get(B[b])
            
            Result.append(abs(alpha-beta))
        

        except StopIteration:
            for d in Result:
                if d == "ZERO":
                    print(d)
                    continue
                RESULT=""
                for k,v in dic.items():
                    while (d-v)>=0:
                        d-=v
                        RESULT+=k
                print(RESULT)
            return


def change(D:list):
    
    dic = {"M":1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1} 
    for d in D:
        if d == "ZERO":
            print(d)
            continue
        Result=""
        for k,v in dic.items():
            while (d-v)>=0:
                d-=v
                Result+=k
        print(Result)
        
#change(calculate())
calculate()