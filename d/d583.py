while True:
    try:
        input()
        print(*sorted(map(int,input().split())))
    except EOFError:
        break

#其實這題應該要用for迴圈比較省記憶體，題目一開始給的N也才能用到
#但這樣比較直覺:)雖然11.2MB 而且我懶了
#企鵝真的很幼稚嘖嘖嘖 :D