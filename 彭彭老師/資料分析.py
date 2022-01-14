import pandas as pd
data = pd.Series( [20,10,15] )
print(data.max) # 取得列表中最大值
data = data*2 
print(data)     # 也可以直接將列表內容*2
data = data==20 # 判斷列表資料是否與目標相符
print(data)  

data2 = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
print(data2)
print( data2["name"] )  # 只取得name這個欄位
print( data2.iloc[0] )  # 印出第一列的資料