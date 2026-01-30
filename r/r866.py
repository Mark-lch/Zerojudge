import sys
def block():
    data=sys.stdin.read().split()

    it=iter(data)

    R=int(next(it))
    C=int(next(it))
    Matrix=[]

    for r in range(R):
        N=[]
        for c in range(C):
            N.append(next(it))
        Matrix.append(N)
        
    Result=1
    r,c=[0,0]
    Matrix[r][c]="0"
    face=[(0,1),(0,-1),(1,0),(-1,0)]

    while r!=R-1 or c!=C-1:
        for a,b in face:
            if not (0 <= r+a < R and 0 <= c+b < C):continue
            elif Matrix[r+a][c+b]=="1":
                r+=a
                c+=b
                Matrix[r][c]="0"
                Result+=1
                break

    print(Result)
        
        
block()