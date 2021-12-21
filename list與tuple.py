nu = [ 90,70,80,60,60,60,1,2,47]
str1 = ["小黑545646","小白","大黑","大白", True]
str2 = "hellow aaaa"

print( nu[2],str1 ) #取得nu第2位
print( nu[1:5] )   #從第1位取得到第五位的值,不含最後一位
print( nu[:4] )    #取得前四位的值
print( str2[0: 4] )    #取得第0位字串
nu.sort()           #由小到大排列
nu.extend( str1 )   #將兩個列表合併
nu.append( 30 )     #將列表再加入一個值
nu.insert(3,50)     #在第3位插入50
nu.remove(90)       #刪除值為90的資料
nu.pop()            #移除列表最後一個資料
nu.reverse()        #將列表反轉
print(nu.index(70))   #回傳70在第幾位
print( nu.count(60))  #找到有幾個60的值
nu.clear()          #將列表清空

str3 = (1,2,4,8,3,25,45,705) #此為tuple
#tuple與list差異為不能更改