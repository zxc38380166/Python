from question import Qusetion
text = [                                                #設計一個題庫
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n ",
    "1公尺=幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是甚麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"
]
questions = [
    Qusetion(text[0],"c"),      #將題庫分別帶入試卷的各屬性(參數1為題目.參數2為答案),並儲存進Qusetion類別
    Qusetion(text[1],"b"),
    Qusetion(text[2],"b"),
]

def run_text(questions):
    score = 0   #設定預設答對題數為0
    for question in questions:      #將試卷的題目用迴圈呈現
        answer = input(question.descoription) #用input將題目呈現出來作為問題
        if answer == question.answer:         #若回答的問題與解答相同則score+1
            score += 1

    print("你得到" + str(score) + "分，滿分為" + str(len(questions)) + "分") # len()函式執行完為數字所以使用str()轉換為字串

run_text(questions) #印出函式