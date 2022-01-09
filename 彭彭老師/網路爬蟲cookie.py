import urllib.request as req
import bs4
def getData(url):
    request = req.Request( url,headers={
        "cookie":"over18=1",                # 將cookie放進標頭
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
    } )
    with req.urlopen( request ) as res:
        data = res.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"html.parser")
    titles = root.find_all("div",class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink = root.find("a",string="‹ 上頁")     # 取得標籤文字含 "< 上頁" 的a標籤
    return nextLink["href"]                       # 取得標籤內的href屬性並回傳出來
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count<5:                                    # 利用迴圈來處理想抓幾頁
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count+=1                                      # 每次執行一次就+1迴圈次數