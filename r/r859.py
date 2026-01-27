time=0
special=False
data=input().split()
prize=input().split()

if prize[6] in  data: 
    special= True

for N in range(6):
    if prize[N] in data:
        time+=1
#print(time,special)

if special: 
    if time==5 :print("B")
    elif time==4 :print("D")
    elif time==3 :print("F")
    elif time==2 :print("G")
    else:print("X")
    
else:
    if time==6:print("A")
    elif time==5:print("C")
    elif time==4:print("E")
    elif time==3:print("H")
    else:print("X")

    