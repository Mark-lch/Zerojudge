import sys
def change():
    data=sys.stdin.read().split()
    it=iter(data)

    while True:
        try:
            R=int(next(it))
            C=int(next(it))

            Matrix=[]
            for r in range(R):
                cc=[]
                for c in range(C):
                    cc.append(next(it))
                Matrix.append(cc)

            NN=[]
            for c in range(C):
                New=[]
                for r in range(R):
                    New.append(Matrix[r][c])
                NN.append(New)
            for row in NN:
                print(*row,sep=" ")
        except StopIteration:
            return


change()
