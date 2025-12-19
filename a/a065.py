Chra=input()
Chra=[ord(_) for _ in Chra]
for a in range(1,len(Chra)):
    print(abs(Chra[a]-Chra[a-1]),end="")