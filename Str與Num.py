from math import * #帶入更多函式
# # 字串的用法
# x = "hellow"          
# print( x.lower() )    #轉成小寫
# print( x.upper() )    #轉成大寫
# print( x.isupper() )  #全是大寫則回傳true
# print( x[0] )         #取得第0位
# print( x.index("h") ) #取得H為第幾位
# print( x.replace("h","H") ) #將第一個參數替換成第二個參數

#數字的用法
y = 8.5
print( y//2 )           #去除小數點的結果
print( y%5 )            #取餘數 8/5 等於1餘3 故取得3
print( "會印出"+str(y) ) #將數字8轉成字串8
print( abs(y) )         #取絕對值,一定為正數
print( pow(y,4) )       #y的4次方
print( max(y,9,4) )     #取得參數內最大的值
print( min(y,1,10) )    #取得參數內最小的值
print( round(y))        #四捨五入
print( floor(y) )       #無條件捨去法
print( ceil(y) )        #無條件進位
print( sqrt(y) )        #開根號