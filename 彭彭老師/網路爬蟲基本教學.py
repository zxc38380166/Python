import urllib.request as req
import bs4 
url = "https://www.ptt.cc/bbs/movie/index.html"
    #建立一個 request 物件並帶入headers標頭,讓我們更像一個使用者來訪問
request = req.Request(url,headers={
      "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
})
with req.urlopen(request) as res:
    data = res.read().decode("utf-8")           # 透過連線抓下來的資料
root = bs4.BeautifulSoup(data,"html.parser")    # 解析資料並告訴bs4要解析的檔案為html
# titles = root.find("div",class_="title")    # find()為找尋標籤  class為title的div標籤
titles = root.find_all("div",class_="title")  #若使用的是find_all則會取得全部class為title的div標籤
# print(titles)                      # 已經找到標籤所以可以直接取得標籤內的子標籤  title下面的a標籤
for title in titles:
    if title.a !=None:               # 如果標題包含a標籤則印出來
        print(title.a.string)