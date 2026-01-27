def search():  
    for a in range(1,len(data)):
        if data[a]==Dict[check+a]:
            continue
        else:
            return False

    else:
        return True
    
input()
Dict=input().split()
data=input().split()
check=-1

while data[0] in Dict[check+1:-1]:
    try:
        check=Dict.index(data[0],check+1)
        if search():
            print(check+1)
            break
    except IndexError:
        pass        
else: print("not found")    