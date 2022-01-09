from flask import Flask
app = Flask(__name__)   # 代表目前執行得模組

@app.route("/")    # 函式的裝飾,以函式為基礎得附加功能,路由器的概念
def home(): 
    return "Hello Flask 2"

@app.route("/test") # 代表要處理的路徑
def test():
    return "This. is Test"

if __name__=="__main__":    # 如果以主程式執行,立即啟動
    app.run()   