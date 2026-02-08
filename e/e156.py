import sys
sys.setrecursionlimit(2000)
N=int(input())
result=0
def SUM(n:int):
    return n and (n+SUM(n-1))
print(SUM(N))
#良心