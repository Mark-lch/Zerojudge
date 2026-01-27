import random as rd
from collections import Counter
import os

def 隨機抽籤():
    Time=int(input("輸入進行幾輪: "))
    frequency=int(input("輸入進行次數: "))
    while Time:
        result=[]
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "people.txt")

        with open(file_path,"r",encoding="utf-8") as f:
            People=[a.strip() for a in f.readlines() if a.strip()]

        for _ in range(frequency):
            result.append(rd.choice(People))

        RESULT=Counter(result)
        print(RESULT)

        Time-=1


"""寒訓名額抽籤"""
#因為本次寒訓為五校聯合，床位只有60，車位68

#因此我們需要釋出兩個名額( 不過因為副社長臨時有事不能參加 所以只需要抽出一個人 )

#而活動報名順序是正社先於地社。

#所以我會用這個抽籤小程式 從 位中抽選出1位非正社同學，將無法參加寒訓，

#
'''
抽籤規則:
檔案"people.txt"中，有5位地社同學的名子，
我會進行 10次 隨機抽籤，
共三輪，
其中被抽到最多次的1位將無法參加寒訓
'''
隨機抽籤()