M,D=map(int,input().split())
if (M*2+D)%3==0: print("普通")
elif (M*2+D)%3==1: print("吉")
else: print("大吉")