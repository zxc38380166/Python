from operator import index
from os import sep
import pandas as pd
data= pd.DataFrame(
    {
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
    }
    ,index=["a","b","c"]
)
print("資料數量",data.size)
print("資料型態()有幾欄幾列",data.shape)
print("資料索引",data.index)
print("取得第二列",data.iloc[1],sep="\n")
print("取得第c列",data.loc["c"],sep="\n" )
print("取得name欄位",data["name"],sep="\n")
salaries = data["salary"]
print("薪水的平均值",salaries.mean() )  # 從雙維資料中取出特定列則變出單維資料(Series),故可以直接使用Series函式做運算
data["revenue"]=[500000,400000,300000] # 建立一個欄並帶入資料
data["rank"]=pd.Series([3,6,1],index=["a","b","c"] )
data["cp"]=data["revenue"]/data["salary"]
print(data)