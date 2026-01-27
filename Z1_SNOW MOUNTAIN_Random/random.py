import random as rd
def 隨機抽籤():
    with open("people.txt","r",encoding="utf-8") as f:
        People=[a.strip() for a in f.readlines() if a.strip()]
    frequency=int(input())
    for b in range(frequency):
        print((rd.choice(People))+"\n")

"""大觀名額抽籤"""
#因為本次大觀要和桃園高中天文社合作，

#兩邊經過商量分配後，因為我們報名人數超出分配名額，需要釋出一個名額。

#而因活動報名順序是正社先於地社。

#所以我會用這個抽籤小程序 從4位中抽選出1位 地社 的同學，他將無法參加本次大觀，

#希望遺憾被抽到的人能理解我們的難處:)
'''
抽籤規則:
檔案"people.txt"中，有四位地社同學的名子，
我會進行 10次 隨機抽籤，
其中被抽到最多次的1位將無法參加本次大觀!
'''
隨機抽籤()