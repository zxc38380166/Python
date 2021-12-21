play = None      #玩家猜測數字預設為none
win = 50         #答案
gameNumber = 0   #用戶輸入次數
gamePlay = 3     #可以輸入幾次
gameOver = False #預設為還沒輸
while play != win and not(gameOver):    
    gameNumber+=1
    if gameNumber<=gamePlay:    
        play = int(input("請輸入數字:"))
        if play<win:
            print("大一點")
        elif play>win:
            print("小一點")
    else:
        gameOver = True

if gameOver:
    print("你輸了")            
else:
    print("你贏了")