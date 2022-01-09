import urllib.request as request            # 載入連線模組
import json                                 # 載入解析json的模組
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")      #取得網頁的原始碼
# print(data)

src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as res:           # 連線至 src
    data = json.load(res)                   # 取得連線後的資料是json格式所以利用模組解析完放入變數data
clist = data["result"]["results"]           # 取得data中的["result"]["results"]
with open("data.txt",mode="w",encoding="utf-8") as file:    #讀取一個新的檔案並寫入
    for company in clist:                   # 因為是列表的關係所以可以用迴圈寫出來
        file.write(company["公司名稱"]+"\n")