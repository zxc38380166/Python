# open("路徑",'mode=模式")
#絕對路徑 C:/Users/zxc38/Desktop/Front-End
#相對路徑 以自身檔案所在位置做延伸
# mode="r" 讀取
# mode="w" 複寫
# mode="a" 在原來的資料後寫東西

# file = open("openText.txt",mode="r")
# for line in file:
#     print(line)           # 利用迴圈將資料一行一行印出來
# print( file.read() )      # 印出全部資料
# print( file.readline() )  # 印出第一行資料
# print( file.readline() )  # 印出第二行資料
# print( file.readlines() ) # 將資料個別放進列表
# file.close() #關掉開啟的檔案釋放資源

# file = open("openText.txt",mode="w")    # w 模式為修改
# file.write("hello")
# file.close() #關掉開啟的檔案釋放資源

# file = open("openText.txt",mode="a",encoding="utf-8")# a 模式為在原有資料加上資料
# file.write("你好,barry")#必須加上utf-8解碼 
# file.close() #關掉開啟的檔案釋放資源

# 以下為省略 close 釋放資源的寫法
with open("openText.txt","w",encoding="utf-8") as file:
    file.write("這是修改後的資料")