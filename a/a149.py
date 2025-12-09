T=input()
NP=[]
for a in range(int(T)):
    NP+=[input()]
    
for c in range(len(NP)):
    Sum=1
    for b in range(len(NP[c])):
        Sum=Sum*int((NP[c])[b])
    print(Sum)