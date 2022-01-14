from operator import index
from os import sep
import pandas as pd
data = pd.Series( [5,4,-2,3,7] ,index=["a","b","c","d","e"])    # index為建立自訂得索引
print("資料型態",data.dtype)    # 數字與字串的函式
print("資料數量",data.size)
print("資料索引",data.index)
print( data[1] )               # 根據順序取得資料
print( data["e"],data["d"] )             # 根據索引取得資料
print("最大值",data.max() )
print("總和",data.sum() )
print("標準差",data.std() )
print("中位數",data.median() )
print("最大3位數",data.nlargest(3) )
print("最小2位數",data.nsmallest(2) )


data2 = pd.Series( ["你好","Python","Pandas"] )
print("算出每一個字串的長度",data2.str.len() )
print("將字串都換成小寫",data2.str.lower() )
print("將字串串接並從參數帶入分隔符號",data2.str.cat(sep="-") )
print("判斷有無包含參數並回傳布林值",data2.str.contains("你好")  )
print("取代字串第一個參數位要取代的,第二個參數為要換得值",data2.str.replace("你好","Hello"))