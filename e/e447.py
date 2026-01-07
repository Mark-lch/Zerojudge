from collections import deque
N=int(input())
queue=deque()
while N>0:
    k=list(map(int,input().split()))
    if k[0]==1:
        queue.append(k[1])
    elif k[0]==2:
        print(queue[0] if queue else -1)
    else:
        if queue:
            queue.popleft()    
    N-=1