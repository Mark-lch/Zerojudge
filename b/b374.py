from collections import Counter
input()
N=list(map(int,input().split()))
N.sort()
#print(N)
res=Counter(N).most_common()

for a in range(len(res)):
    if res[a][1]==res[0][1]:
        print(*res[a])